import duckdb

print(
    duckdb.query(
        """
    INSTALL fakeit FROM community;
    LOAD fakeit;
    
    CREATE OR REPLACE TABLE orders AS 
    SELECT
        DATE '2025-01-01' + CAST(random() * 365 AS INTEGER) AS order_date,
        fakeit_uuid_v4() as order_uuid,
        fakeit_uuid_v4() as customer_uuid,
        fakeit_uuid_v4() as employee_uuid,
        fakeit_address_city() AS city,
        fakeit_currency_price()::FLOAT as amount,
        fakeit_payment_credit_card_type() as payment_method
    FROM
        generate_series(1, 1_000_000)
    """
    )
)

duckdb.query("SET memory_limit TO '1GB';")


print(
    duckdb.query(
        """
        SELECT value AS memlimit
        FROM duckdb_settings()
        WHERE name = 'memory_limit'; 
        """
    )
)

