import duckdb
from duckdb.sqltypes import INTEGER
from random import randint


def generate_random_value():
    return randint(a=1, b=10_000)


duckdb.create_function(
    name="generate_random_value",
    function=generate_random_value,
    parameters=None,
    return_type=INTEGER,
)

print(duckdb.query("SELECT generate_random_value() AS value"))
