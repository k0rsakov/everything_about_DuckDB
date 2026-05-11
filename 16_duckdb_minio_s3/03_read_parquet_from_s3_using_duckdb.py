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


print(
    con.query(
        """ 
        SELECT count()
        FROM 's3://prod/yellow_tripdata/2025/12/data.parquet';
        """
    )
)

print(
    con.query(
        """
        SELECT *
        FROM 's3://prod/yellow_tripdata/2025/12/data.parquet'
        LIMIT 5;
        """
    )
)
