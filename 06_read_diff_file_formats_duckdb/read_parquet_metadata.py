import duckdb

print(duckdb.query("DESCRIBE SELECT * FROM 'fake_data.parquet';"))

print(duckdb.query("DESCRIBE SELECT * FROM parquet_metadata('fake_data.parquet');"))
