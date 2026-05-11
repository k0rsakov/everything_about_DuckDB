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

# 2020-2021-2022
print(
    con.query(
        """
        SELECT
            date_trunc('year', tpep_pickup_datetime) AS pickup_year,
            COUNT(*) AS trip_count
        FROM
            's3://prod/yellow_tripdata/202[0-2]/*/data.parquet'
        WHERE
            1=1
        GROUP BY
            1
        -- Исключение выбросов
        HAVING
            trip_count > 1_000
        ORDER BY
            1
        """
    )
)

# 2023-2024-2025
print(
    con.query(
        """
        SELECT
            date_trunc('year', tpep_pickup_datetime) AS pickup_year,
            COUNT(*) AS trip_count
        FROM
            's3://prod/yellow_tripdata/202[3-5]/*/data.parquet'
        WHERE
            1=1
        GROUP BY
            1
        -- Исключение выбросов
        HAVING
            trip_count > 1_000
        ORDER BY
            1
        """
    )
)

# 2020-2022-2024, чётные года
print(
    con.query(
        """
        SELECT
            date_trunc('year', tpep_pickup_datetime) AS pickup_year,
            COUNT(*) AS trip_count
        FROM
            's3://prod/yellow_tripdata/202[0,2,4]/*/data.parquet'
        WHERE
            1=1
        GROUP BY
            1
        -- Исключение выбросов
        HAVING
            trip_count > 1_000
        ORDER BY
            1
        """
    )
)

print(
    con.query(
        """
        SELECT
            date_trunc('year', tpep_pickup_datetime) AS pickup_year,
            EXTRACT(QUARTER FROM date_trunc('year', tpep_pickup_datetime)) AS pickup_quarter,
            COUNT(*) AS trip_count
        FROM
            's3://prod/yellow_tripdata/*/0[1-3]/data.parquet'
        WHERE
            1=1
        GROUP BY
            1, 2
        -- Исключение выбросов
        HAVING
            trip_count > 1_000
        ORDER BY
            1, 2
        """
    )
)

# 2020-2025, январь-февраль-декабрь (зима)
print(
    con.query(
        """
        SELECT
            date_trunc('year', tpep_pickup_datetime) AS pickup_year,
            date_trunc('month', tpep_pickup_datetime) AS pickup_month,
            COUNT(*) AS trip_count
        FROM
            read_parquet(
                [
                    's3://prod/yellow_tripdata/*/01/data.parquet',
                    's3://prod/yellow_tripdata/*/02/data.parquet',
                    's3://prod/yellow_tripdata/*/12/data.parquet'
                ]
            )
        WHERE
            1=1
            AND tpep_pickup_datetime BETWEEN '2020-01-01' AND '2026-01-01'
        GROUP BY
            1, 2
        ORDER BY
            1, 2
        """
    )
)

# Исследование выбросов за период 2020-2021-2022
print(
    con.query(
        """
        SELECT
            filename,
            date_trunc('year', tpep_pickup_datetime) AS pickup_year,
            COUNT(*) AS trip_count
        FROM
            's3://prod/yellow_tripdata/202[0-2]/*/data.parquet'
        WHERE
            1=1
        GROUP BY
            1, 2
        ORDER BY
            2
        """
    )
)
