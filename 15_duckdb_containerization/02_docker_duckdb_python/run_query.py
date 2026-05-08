import sys
import duckdb


def main():
    if len(sys.argv) != 2:
        print("Usage: run_query.py <SQL_QUERY>")
        sys.exit(1)
    sql_query = sys.argv[1]
    # Создаем подключение к DuckDB
    con = duckdb.connect()
    try:
        # Выполняем SQL-запрос
        result = con.execute(sql_query).fetchall()
        # Выводим результат
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        # Закрываем подключение
        con.close()


if __name__ == "__main__":
    main()
