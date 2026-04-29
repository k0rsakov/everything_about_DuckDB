import duckdb

print(duckdb.query("SELECT * FROM 'fake_data.parquet'"))
