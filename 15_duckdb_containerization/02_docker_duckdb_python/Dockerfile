# Используем базовый образ с Python 3.12
FROM python:3.13-slim

# Устанавливаем DuckDB
RUN pip install duckdb==1.5.1

# Копируем скрипт для выполнения SQL-запроса
COPY run_query.py /usr/src/app/run_query.py

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Указываем команду для запуска контейнера
ENTRYPOINT ["python", "run_query.py"]