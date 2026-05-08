# Образ DuckDB через CLI

Для сборки образа используется команда:

```bash
docker build -t duckdb-cli .
```

Для вызова команд в контейнере используется команда:

```bash
docker run --rm -it duckdb-cli -c "<команда>"
```