import duckdb

con = duckdb.connect()

con.query(
    """
    INSTALL httpfs;
    LOAD httpfs;
    SET s3_endpoint = 'localhost:9000';
    SET s3_use_ssl = false;
    SET s3_url_style = 'path';
    SET s3_access_key_id = 'minioadmin';
    SET s3_secret_access_key = 'minioadmin';
    """
)

# .csv, .parquet
con.query(
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
        generate_series(1, 1_000_000);
    
    COPY fake_data TO 's3://prod/fake_data/fake_data.csv' (FORMAT 'CSV');
    COPY fake_data TO 's3://prod/fake_data/fake_data.parquet' (FORMAT 'PARQUET');
    """
)

df_csv = con.query(
    """
    EXPLAIN ANALYZE
    SELECT count() FROM 's3://prod/fake_data/fake_data.csv' 
    """
).df()

df_parquet = con.query(
    """
    EXPLAIN ANALYZE
    SELECT count() FROM 's3://prod/fake_data/fake_data.parquet' 
    """
).df()

print("🧾 CSV:")
print(df_csv.explain_value[0])

print("\n🪵 PARQUET:")
print(df_parquet.explain_value[0])

con.close()
