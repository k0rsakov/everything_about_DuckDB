import duckdb

con = duckdb.connect()

con.query(
    """
    INSTALL httpfs;
    LOAD httpfs;
    SET s3_endpoint = 'localhost:9000';
    SET s3_use_ssl = false;
    SET s3_url_style = 'path';
    SET s3_access_key_id = 'minioadmin';
    SET s3_secret_access_key = 'minioadmin';
    """
)

print("Чтение конкретного файла .parquet:")
print(con.query("SELECT count() FROM 's3://prod/fake_data/fake_data.parquet';"))

print("Чтение конкретного файла .csv:")
print(con.query("SELECT count() FROM 's3://prod/fake_data/fake_data.csv';"))

print("Чтение всех файлов .parquet:")
print(con.query("SELECT count() FROM 's3://prod/fake_data/*.parquet';"))

print("Чтение всех файлов .csv:")
print(con.query("SELECT count() FROM 's3://prod/fake_data/*.csv';"))
