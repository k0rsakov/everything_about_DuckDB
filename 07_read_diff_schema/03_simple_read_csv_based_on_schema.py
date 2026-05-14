import duckdb

print(duckdb.query("SELECT * FROM read_csv('*.csv', union_by_name=true)"))
