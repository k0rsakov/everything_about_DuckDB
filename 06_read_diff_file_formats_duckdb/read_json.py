import duckdb

print(duckdb.query("SELECT * FROM 'fake_data.json'"))

print(duckdb.query("SELECT json.users FROM 'fake_data.json'"))

print(duckdb.query("SELECT UNNEST(json.users).name FROM 'fake_data.json'"))
