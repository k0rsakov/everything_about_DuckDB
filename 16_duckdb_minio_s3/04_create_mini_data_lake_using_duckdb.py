import time

import duckdb


base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
s3_path = "s3://prod/yellow_tripdata"
start_year = 2020
end_year = 2025

print(f"🚀 Начинаю загрузку данных Yellow Taxi за {start_year}-{end_year} гг...")

for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        # Форматируем месяц с ведущим нулем (например, 01, 02...)
        month_str = f"{month:02d}"

        # Формируем имя файла и URL
        file_name = f"yellow_tripdata_{year}-{month_str}.parquet"
        url = f"{base_url}/{file_name}"

        # Целевой путь в MinIO с партиционированием
        target_s3_key = f"{s3_path}/{year}/{month_str}/data.parquet"

        print(f"📦 Обработка: {year}-{month_str}...")

        try:
            # Основной запрос: читаем по ссылке -> пишем в S3
            duckdb.query(
                f"""
                INSTALL httpfs;
                LOAD httpfs;
                SET s3_endpoint = 'localhost:9000';
                SET s3_use_ssl = false;
                SET s3_url_style = 'path';
                SET s3_access_key_id = 'minioadmin';
                SET s3_secret_access_key = 'minioadmin';
                
                COPY
                (
                    SELECT *
                    FROM '{url}'
                )
                TO '{target_s3_key}' (FORMAT 'PARQUET');
            """)
            print(f"✅ Успешно: {target_s3_key}")
        except Exception as e:
            # Обработка случаев, если данных за конкретный месяц еще нет (например, конец 2025)
            print(f"⚠️ Ошибка при загрузке {year}-{month_str}: {e}")
time.sleep(3)
print("\n✨ Загрузка завершена!")
