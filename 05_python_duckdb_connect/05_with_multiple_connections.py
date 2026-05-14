import duckdb

connection_0 = duckdb.connect()
connection_1 = duckdb.connect()

connection_0.query("CREATE TABLE numbers AS SELECT * FROM range(5)")
connection_1.query("CREATE TABLE numbers AS SELECT * FROM range(10)")

print("Таблица numbers в connection_0:\n", connection_0.query("SELECT * FROM numbers"))
print("Таблица numbers в connection_1:\n", connection_1.query("SELECT * FROM numbers"))

connection_0.close()
connection_1.close()
