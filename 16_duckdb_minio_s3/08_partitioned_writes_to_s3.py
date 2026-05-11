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

con.query(
    """
    CREATE OR REPLACE TABLE parquet_data AS
    SELECT
        *,
        EXTRACT(YEAR FROM tpep_pickup_datetime) AS year,
        EXTRACT(MONTH FROM tpep_pickup_datetime) AS month
    FROM
        's3://prod/yellow_tripdata/2020/01/data.parquet'
    """
)

con.query(
    """
    COPY parquet_data TO 's3://prod/partition_yellow_tripdata/'
    (FORMAT parquet, PARTITION_BY (year, month), OVERWRITE_OR_IGNORE);
    """
)

print(
    con.query(
        "SELECT count() FROM 's3://prod/partition_yellow_tripdata/*/*/*.parquet' LIMIT 5;"
    )
)

print(
    con.query(
        """
        SELECT
            count()
        FROM
            's3://prod/partition_yellow_tripdata/*/*/*.parquet'
        WHERE
            year = 2021;
        """
    )
)

df_explain = con.query(
    """
    EXPLAIN ANALYZE
    SELECT
        count()
    FROM
        's3://prod/partition_yellow_tripdata/*/*/*.parquet'
    WHERE
        year = 2021;
    """
).df()

print(df_explain.explain_value[0])
