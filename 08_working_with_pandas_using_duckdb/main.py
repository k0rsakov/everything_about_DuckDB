import pandas as pd
import duckdb
from random import randint

df = pd.DataFrame.from_dict(
    {
        "id": [i for i in range(10)],
        "value": [randint(a=100, b=10000) for _ in range(10)],
    }
)

print(
    "DuckDB позволяет читать переменные из Python потока:\n",
    duckdb.query("SELECT * FROM df"),
)

print(
    "Выполнение фильтрации в df без физических изменений:\n",
    duckdb.query(
        """
        SELECT
            *
        FROM
            df
        WHERE
            1=1
            AND value <= 1000
        """
    ),
)

df_filtered_by_duckdb = duckdb.query(
    """
    SELECT
        *
    FROM
        df
    WHERE
        1=1
        AND value >= 1000
    """
).df()

print(
    "Новый физически созданный pd.DataFrame с фильтрацией через DuckDB:\n",
    df_filtered_by_duckdb,
)

df_filtered_by_pandas = df[df["value"] >= 1000]
print(
    "Новый физически созданный pd.DataFrame с фильтрацией через Pandas:\n",
    df_filtered_by_pandas,
)
