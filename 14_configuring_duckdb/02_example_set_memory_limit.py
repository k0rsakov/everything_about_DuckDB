import duckdb

import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"Функция {func.__name__} выполнилась за {execution_time:.6f} секунд")

        return result

    return wrapper


@measure_time
def create_orders_dataset():
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
            generate_series(1, 15_000_000);
        """
    )


create_orders_dataset()

print("Текущий лимит памяти:")

print(
    duckdb.query(
        """
        SELECT value AS memlimit
        FROM duckdb_settings()
        WHERE name = 'memory_limit'; 
        """
    )
)


@measure_time
def execute_sort_without_limit():
    duckdb.query(
        """
        CREATE OR REPLACE TABLE sorted_orders AS 
        SELECT * 
        FROM orders
        ORDER BY
            city,
            amount DESC,
            order_date;
        """
    )


execute_sort_without_limit()

duckdb.query("SET memory_limit TO '1GB';")

print("\n\nТекущий лимит памяти после установки ограничения:")

print(
    duckdb.query(
        """
        SELECT value AS memlimit
        FROM duckdb_settings()
        WHERE name = 'memory_limit'; 
        """
    )
)


@measure_time
def execute_sort_with_limit():
    duckdb.query(
        """
        CREATE OR REPLACE TABLE sorted_orders_limited AS 
        SELECT *
        FROM orders 
        ORDER BY
            city,
            amount DESC,
            order_date;
        """
    )


execute_sort_with_limit()
