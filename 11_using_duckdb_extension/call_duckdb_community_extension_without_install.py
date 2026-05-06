import duckdb


print(
    duckdb.query(
        """
        SELECT
            fakeit_name_full() AS name
        """
    )
)
