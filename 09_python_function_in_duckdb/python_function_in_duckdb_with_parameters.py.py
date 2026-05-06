import duckdb
from duckdb.sqltypes import BIGINT, BOOLEAN
from random import randint


def check_parity(value: int | None = None) -> bool:
    return value % 2 == 0


duckdb.create_function(
    name="check_parity",
    function=check_parity,
    parameters=[BIGINT],
    return_type=BOOLEAN,
)

print(duckdb.query("SELECT check_parity(1) AS check_parity"))
print(duckdb.query("SELECT check_parity(10) AS check_parity"))
