import duckdb

print(
    "Список доступных расширений в DuckDB:\n",
    duckdb.query(
        """
        SELECT extension_name, description FROM duckdb_extensions();
        """
    ).df(),
)

duckdb.query(
    """
    INSTALL airport FROM community;
    LOAD airport;
    """
)

print(
    "\n\n\nСписок доступных расширений в DuckDB:\n",
    duckdb.query(
        """
        SELECT extension_name, description FROM duckdb_extensions();
        """
    ).df(),
)
