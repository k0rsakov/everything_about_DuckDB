import duckdb

connection = duckdb.connect()

print(connection.query("SELECT 1 AS one"))

connection.close()
