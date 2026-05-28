# Конфигурирование DuckDB

Документация:

- [Python API](https://duckdb.org/docs/current/clients/python/overview)
- [Python DB API](https://duckdb.org/docs/current/clients/python/dbapi)
- [Performance Guide](https://duckdb.org/docs/current/guides/performance/overview)
    - [Spilling to Disk](https://duckdb.org/docs/current/guides/performance/how_to_tune_workloads#spilling-to-disk)
    - [My Workload Is Slow](https://duckdb.org/docs/current/guides/performance/my_workload_is_slow)
- [Configuration](https://duckdb.org/docs/current/configuration/overview)
  - [Global Configuration Options](https://duckdb.org/docs/current/configuration/overview#global-configuration-options)

> **_Note:_**
> По своей природе DuckDB "_ест_" все ресурсы, что увидит. Поэтому если не ограничивать DuckDB в ресурсах, то он может
> одномоментно загрузить 100Gb RAM вычислениями.
>
> **Задача DuckDB — быстро считать.**