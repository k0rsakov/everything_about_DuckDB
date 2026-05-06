import duckdb
import pandas as pd

pd.set_option("display.max_columns", None)

print(
    duckdb.query(
        """
        INSTALL http_client FROM community;
        LOAD http_client;

        WITH response AS (
            -- Выполняем запрос    
            SELECT
                http_get('https://randomuser.me/api/') AS res
        ), parsed_body AS (
            -- Извлекаем тело и преобразуем его в JSON
            SELECT
                (res->>'body')::JSON AS raw_body
            FROM
                response
        ), list_conversion AS (
            -- Преобразуем JSON-массив в LIST
            SELECT
                from_json(
                    raw_body,
                    '{"results": "JSON[]"}'
                ).results AS results_list
            FROM
                parsed_body
        ), unpacked AS (
            -- Распаковываем список
            SELECT
                unnest(results_list) AS user_data
            FROM
                list_conversion
        )
        -- Основной запрос на чтение ключей
        SELECT
            user_data ->> '$.name.first' AS first_name,
            user_data ->> '$.name.last' AS last_name,
            user_data ->> '$.gender' AS gender,
            user_data ->> '$.location.country' AS country,
            user_data ->> '$.location.city' AS city,
            user_data ->> '$.email' AS email,
            user_data ->> '$.phone' AS phone
        FROM
            unpacked;
        """
    ).df()
)
