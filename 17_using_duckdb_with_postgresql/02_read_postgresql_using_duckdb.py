import duckdb

con = duckdb.connect()

con.query(
    "ATTACH "
    "'dbname=postgres "
    "user=postgres "
    "host=localhost "
    "password=postgres' "
    "AS db (TYPE postgres, SCHEMA 'public');"
)

print(
    con.query(
        """
        SELECT *
        FROM db.tbl
        """
    )
)
