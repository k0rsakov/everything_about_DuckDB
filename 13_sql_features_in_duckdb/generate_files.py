import duckdb

duckdb.query(
    """
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

    COPY fake_data TO 'fake_data.parquet';
    """
)

