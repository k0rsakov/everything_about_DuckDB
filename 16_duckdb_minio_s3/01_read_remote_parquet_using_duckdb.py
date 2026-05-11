import duckdb

duckdb.query(
    """
    CREATE OR REPLACE TABLE yellow_tripdata AS
    SELECT *
    FROM 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-12.parquet'
    """
)

print(duckdb.query("SELECT count() FROM yellow_tripdata;"))

print(duckdb.query("SELECT * FROM yellow_tripdata LIMIT 5;"))
