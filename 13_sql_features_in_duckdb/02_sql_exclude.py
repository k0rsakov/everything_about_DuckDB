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
    "Получение всех колонок, кроме email и city:\n",
    duckdb.query(
        """
        SELECT * EXCLUDE (email, city) FROM 'fake_data.parquet'
        """
    ),
)
