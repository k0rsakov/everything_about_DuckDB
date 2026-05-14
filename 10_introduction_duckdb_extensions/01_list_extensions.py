import duckdb

print(
    "Список доступных расширений в DuckDB:\n",
    duckdb.query(
        """
        SELECT extension_name, description FROM duckdb_extensions();
        """
    ).df(),
)
