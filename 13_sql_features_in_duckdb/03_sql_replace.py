import duckdb

print(
    "Все колонки:\n",
    duckdb.query(
        """
        SELECT * FROM 'fake_data.parquet'
        """
    ),
)

print(
    "Замена значения колонки country на верхний регистр:\n",
    duckdb.query(
        """
        SELECT * REPLACE (upper(country) AS country) FROM 'fake_data.parquet'
        """
    ),
)
