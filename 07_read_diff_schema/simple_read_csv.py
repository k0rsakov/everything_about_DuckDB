import duckdb

print(duckdb.query("SELECT * FROM '*.csv'"))
