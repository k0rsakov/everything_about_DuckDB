import duckdb


# .csv
duckdb.query(
    """
    INSTALL fakeit FROM community;
    LOAD fakeit;
    
    COPY
    (
        SELECT
            fakeit_name_full() AS name,
            fakeit_contact_email() AS email,
            fakeit_address_city() AS city
    )
    TO 'fake_data_0.csv';
    
    COPY
    (
        SELECT
            fakeit_name_full() AS name,
            fakeit_contact_email() AS email,
            fakeit_address_city() AS city,
            fakeit_address_country() AS country
    )
    TO 'fake_data_1.csv';
    """
)


