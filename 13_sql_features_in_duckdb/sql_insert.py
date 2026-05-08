import duckdb
import pandas as pd

pd.set_option("display.max_columns", None)
duckdb.query(
    """
    CREATE TABLE users
    (
        id INTEGER,
        first_name VARCHAR,
        middle_name VARCHAR,
        last_name VARCHAR,
        email VARCHAR,
        birth_date DATE
    )
    """
)

print("Первый запрос к таблице users:\n", duckdb.query("SELECT * FROM users"))

duckdb.query(
    """
    INSERT INTO users
    (
        id,
        first_name,
        middle_name,
        last_name,
        email,
        birth_date
    )
    VALUES
    (
        1,
        'John',
        'A.',
        'Doe',
        'john.doe@example.com',
        '1990-01-01'
    )
    """
)


print("Таблица после обычной вставки данных:\n", duckdb.query("SELECT * FROM users"))

duckdb.query(
    """
    INSERT INTO users
    (
        id,
        first_name,
        middle_name,
        last_name,
        email,
        birth_date
    )
    VALUES
    (
        2,
        'Bay',
        'john.doe@example.com',
        'Fill',
        'Q.',
        '1999-07-15'
    )
    """
)

print(
    "Таблица после обычной вставки данных в неверном порядке:\n",
    duckdb.query("SELECT * FROM users"),
)

duckdb.query(
    """
    INSERT INTO users BY NAME
    (
    SELECT
        3 AS id,
        'Alice' AS first_name,
        'B.' AS middle_name,
        'Smith' AS last_name,
        'alice.smith@example.com' AS email,
        '1992-03-09' AS birth_date
    );
    INSERT INTO users BY NAME
    (
    SELECT
        4 AS id,
        'Kirsten' AS first_name,
        'B.' AS middle_name,
        'Sipes' AS last_name,
        'coybins@schumm.name' AS email
    )
    """
)

print(
    "Таблица после вставки данных с помощью BY NAME:\n",
    duckdb.query("SELECT * FROM users"),
)
