# Взаимодействие с расширением `pg_duckdb` в PostgreSQL

Документация:

- [Python API](https://duckdb.org/docs/current/clients/python/overview)
- [Python DB API](https://duckdb.org/docs/current/clients/python/dbapi)
- Чтение файлов:
    - [Parquet](https://duckdb.org/docs/current/data/parquet/overview)
- [COPY Statement](https://duckdb.org/docs/current/sql/statements/copy)
- [PostgreSQL Extension](https://duckdb.org/docs/current/core_extensions/postgres)
    - [Querying Postgres Tables Directly from DuckDB](https://duckdb.org/2022/09/30/postgres-scanner)
- [pg_duckdb](https://github.com/duckdb/pg_duckdb)
    - [DockerHub pgduckdb/pgduckdb](https://hub.docker.com/r/pgduckdb/pgduckdb)
- [Data Types](https://duckdb.org/docs/current/sql/data_types/overview)

## Сборка проекта

```bash
docker compose up -d
```

## Demo SQL

```sql
SET duckdb.force_execution = false;
EXPLAIN ANALYZE SELECT count(*) FROM public.tbl;

SET duckdb.force_execution = true;
EXPLAIN ANALYZE SELECT count(*) FROM public.tbl;

SET duckdb.force_execution = true;
EXPLAIN ANALYZE 
SELECT * FROM public.tbl
WHERE 1=1
AND city = 'Blockton';

SET duckdb.force_execution = false;
EXPLAIN ANALYZE 
SELECT * FROM public.tbl
WHERE 1=1
AND city = 'Blockton';
```