# Образ DuckDB через Python

Для сборки образа используется команда:

```bash
docker build -t duckdb-python .
```

Для вызова команд в контейнере используется команда:

```bash
docker run --rm -it duckdb-python "<команда>"
```