import duckdb

connection = duckdb.connect()

connection.query("CREATE TABLE numbers AS SELECT * FROM range(5)")

print(connection.query("SELECT * FROM information_schema.tables"))

print(connection.query("SELECT * FROM numbers"))

connection.close()
