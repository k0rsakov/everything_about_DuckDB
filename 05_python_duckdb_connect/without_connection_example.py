import duckdb

print(duckdb.query("CREATE TABLE numbers AS SELECT * FROM range(5)"))

print(duckdb.query("SELECT * FROM information_schema.tables"))

print(duckdb.query("SELECT * FROM numbers"))
