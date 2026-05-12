import duckdb

con = duckdb.connect()

con.query(
    "ATTACH "
    "'dbname=postgres "
    "user=postgres "
    "host=localhost "
    "password=postgres' "
    "AS db (TYPE postgres, SCHEMA 'public');"
)

con.query(
    """
    DROP TABLE IF EXISTS db.tbl;
    CREATE TABLE db.tbl
    (
        id INT8 PRIMARY KEY,
        name VARCHAR,
        email VARCHAR,
        city VARCHAR,
        country VARCHAR
    );
    """
)

con.query(
    """
    INSTALL fakeit FROM community;
    LOAD fakeit;
    
    INSERT INTO db.tbl
    SELECT
        s.id AS id,
        fakeit_name_full() AS name,
        fakeit_contact_email() AS email,
        fakeit_address_city() AS city,
        fakeit_address_country() AS country
    FROM
        generate_series(1, 100) AS s(id);
    """
)
