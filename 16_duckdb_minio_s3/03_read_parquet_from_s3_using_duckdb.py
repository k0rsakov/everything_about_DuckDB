import duckdb

print(
    duckdb.query(
        """
        SET s3_endpoint = 'localhost:9000';
        SET s3_use_ssl = false;
        SET s3_url_style = 'path';
        SET s3_access_key_id = 'minioadmin';
        SET s3_secret_access_key = 'minioadmin';
        
        SELECT count()
        FROM 's3://prod/yellow_tripdata/2025/12/data.parquet';
        """
    )
)

print(
    duckdb.query(
        """
        SET s3_endpoint = 'localhost:9000';
        SET s3_use_ssl = false;
        SET s3_url_style = 'path';
        SET s3_access_key_id = 'minioadmin';
        SET s3_secret_access_key = 'minioadmin';
    
        SELECT *
        FROM 's3://prod/yellow_tripdata/2025/12/data.parquet'
        LIMIT 5;
        """
    )
)
