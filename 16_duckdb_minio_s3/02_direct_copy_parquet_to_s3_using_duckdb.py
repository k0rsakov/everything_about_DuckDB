import duckdb

duckdb.query(
    """
    --INSTALL httpfs;
    --LOAD httpfs;

    SET s3_endpoint = 'localhost:9000';
    SET s3_use_ssl = false;
    SET s3_url_style = 'path';
    SET s3_access_key_id = 'minioadmin';
    SET s3_secret_access_key = 'minioadmin';
    
    COPY
    (
        SELECT *
        FROM 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-12.parquet'
    )
    TO 's3://prod/yellow_tripdata_example/2025/12/data.parquet'
    """
)
