import duckdb


print(
    duckdb.query(
        """
        SELECT extension_name, install_path
        FROM duckdb_extensions()
        WHERE 1=1
        AND extension_name = 'airport';
        """
    )
)
