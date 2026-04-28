import duckdb


# .csv, .parquet
duckdb.query(
    '''
    INSTALL fakeit FROM community;
    LOAD fakeit;
    
    CREATE TABLE fake_data AS
    SELECT
        fakeit_name_full() AS name,
        fakeit_contact_email() AS email,
        fakeit_address_city() AS city,
        fakeit_address_country() AS country
    FROM
        generate_series(1, 100);
    
    COPY fake_data TO 'fake_data.csv';
    COPY fake_data TO 'fake_data.parquet';
    '''
)

# .json

duckdb.query(
"""
    COPY
    (
        SELECT
            json_object(
                'type',
                'User',
                'users',
                json_group_array(
                    json_object(
                        'name', fakeit_name_full(),
                        'city', fakeit_address_city(),
                        'country', fakeit_address_country()
        )
      )
    ) AS json
    FROM generate_series(1, 10)
    ) TO 'fake_data.json'
    """
)