import duckdb

print(
    "Список доступных расширений в DuckDB:\n",
    duckdb.query(
        """
        SELECT loaded, installed, install_path
        FROM duckdb_extensions()
        WHERE 1=1
        AND extension_name = 'tpch' 
        """
    ),
)

print(
    "Список текущих таблиц:\n",
    duckdb.query(
        """
        SHOW TABLES;
        """
    ),
)

print(
    "Результат запроса к расширению tpch:\n",
    duckdb.query(
        """
        CALL dbgen(sf = 1);
        """
    ),
)

print(
    "Список текущих таблиц:\n",
    duckdb.query(
        """
        SHOW TABLES;
        """
    ),
)

print(
    duckdb.query(
        """
        SELECT
            o_orderdate,
            count(o_orderkey) AS cnt_orders,
            sum(o_totalprice) AS sum_orders
        FROM
            orders
        WHERE
            1=1
        GROUP BY
            1;
    """
    )
)
