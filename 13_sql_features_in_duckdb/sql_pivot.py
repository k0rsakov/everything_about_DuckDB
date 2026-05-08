import duckdb
import pandas as pd

pd.set_option("display.max_columns", None)

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


print(
    duckdb.query(
        """
        PIVOT (
            SELECT
                strftime(order_date, '%Y-%m') AS month,
                amount
            FROM orders
        )
        ON month
        USING sum(amount)
        """
    )
)

print(
    duckdb.query(
        """
        PIVOT orders
        ON payment_method
        USING sum(amount)
        GROUP BY city
        """
    )
)
