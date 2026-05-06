import duckdb


print(
    duckdb.query(
        """
        INSTALL fakeit FROM community;
        LOAD fakeit;
        SELECT
            fakeit_name_full() AS name
        """
    )
)
