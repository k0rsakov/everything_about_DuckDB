# Использование официального образа DuckDB

Документация:

- [DuckDB Docker Container](https://duckdb.org/docs/current/operations_manual/duckdb_docker)

Если вы не хотите устанавливать DuckDB на свою машину, то вы можете использовать официальный образ DuckDB для запуска
контейнера с DuckDB.

Для запуска контейнера с DuckDB используется команда:

```bash
docker run --rm -it -v "$(pwd):/workspace" -w /workspace duckdb/duckdb:1.5.1
```

Если вы хотите использовать образ как "_ручку_", что было показано в примерах:
- [01_docker_duckdb_cli](../01_docker_duckdb_cli)
- [02_docker_duckdb_python](../02_docker_duckdb_python)

Используйте команду:

```bash
echo "SELECT 42;" | docker run --rm -i duckdb/duckdb:1.5.1
```
