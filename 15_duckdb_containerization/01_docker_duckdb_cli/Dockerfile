# Используем базовый образ с Debian для x86_64
FROM --platform=linux/amd64 debian:latest

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y curl unzip

# Скачиваем и распаковываем DuckDB
RUN curl --fail --location --progress-bar --output duckdb_cli-linux-amd64.zip https://github.com/duckdb/duckdb/releases/download/v1.5.1/duckdb_cli-linux-amd64.zip && \
    unzip duckdb_cli-linux-amd64.zip && \
    mv duckdb /usr/local/bin/duckdb && \
    rm duckdb_cli-linux-amd64.zip

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Указываем команду для запуска контейнера
ENTRYPOINT ["duckdb"]