import time
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

base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
s3_path = "s3://prod/yellow_tripdata"
start_year = 2020
end_year = 2025

print(f"🚀 Начинаю загрузку данных Yellow Taxi за {start_year}-{end_year} гг...")

for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        month_str = f"{month:02d}"
        file_name = f"yellow_tripdata_{year}-{month_str}.parquet"
        url = f"{base_url}/{file_name}"
        target_s3_key = f"{s3_path}/{year}/{month_str}/data.parquet"

        try:
            # Пытаемся просто проверить наличие файла через описание (самый быстрый способ)
            con.query(f"SELECT 1 FROM '{target_s3_key}' LIMIT 1")
            print(f"✅ Пропускаю {year}-{month_str} (уже загружено)")

        except (duckdb.IOException, duckdb.HTTPException):
            # Если файла нет (404), DuckDB бросит ошибку — значит, нужно загружать
            print(f"📦 Обработка: {year}-{month_str}...")
            try:
                con.query(
                    f"""
                    COPY (SELECT * FROM '{url}') 
                    TO '{target_s3_key}' (FORMAT 'PARQUET');
                    """
                )
                print(f"✅ Успешно загружено: {target_s3_key}")
            except Exception as e:
                # На случай, если данных еще нет на сайте NYC TLC (например, будущие месяцы)
                print(f"⚠️ Ошибка (возможно, данных нет на источнике): {year}-{month_str}")

    # Спим после каждого года, чтобы не "пугать" API источника
    time.sleep(3)
    print(f"\n--- Год {year} обработан ---")

con.close()
print("\n✨ Загрузка полностью завершена!")