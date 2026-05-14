import duckdb
import pandas as pd

pd.set_option("display.max_columns", None)
print(duckdb.query("SUMMARIZE fake_data.parquet").df())
