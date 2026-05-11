import duckdb

print(
    duckdb.query(
        """
        SELECT value AS memlimit
        FROM duckdb_settings()
        WHERE name = 'memory_limit';
        """
    )
)

duckdb.query("SET memory_limit TO '1GB';")


print(
    duckdb.query(
        """
        SELECT value AS memlimit
        FROM duckdb_settings()
        WHERE name = 'memory_limit'; 
        """
    )
)
