import duckdb

con = duckdb.connect()

df_csv = con.query(
    """
    EXPLAIN ANALYZE
    SELECT count() FROM 'fake_data.csv' 
    """
).df()

df_parquet = con.query(
    """
    EXPLAIN ANALYZE
    SELECT count() FROM 'fake_data.parquet' 
    """
).df()

print("🧾 CSV:")
print(df_csv.explain_value[0])

print("\n🪵 PARQUET:")
print(df_parquet.explain_value[0])

con.close()
