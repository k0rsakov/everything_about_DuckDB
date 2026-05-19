# Возможности и рецепты DuckDB

В данном разделе будут рассмотрены те моменты, которые вам могут помочь на практике при работе с данными.

## Сэмплирование данных

В DuckDB довольно мощный движок для работы с сэмплированными данными. При использовании сэмплирования, анализ данных
происходит намного быстрее, потому что вы не используете все данные.

Данный функционал позволяет оптимизировать OLAP нагрузку.

Документация:

- [Samples](https://duckdb.org/docs/current/sql/samples)

## Тип данных enum (перечисления)

При использовании DuckDB как вычислителя стоит обратить внимание на такой тип данных как перечисления. Он позволяет
создать словарь с низко-кардинальными значениями.

Грубо говоря, данный функционал позволяет вам создать хэш-таблицу, по которой сможете быстрее фильтроваться.

Документация:

- [Enum Data Type](https://duckdb.org/docs/current/sql/data_types/enum)

## Обновление значений (`UPDATE`)

`UPDATE` работает, но классический подход в виде `UPSERT` будет в разы эффективнее.

DuckDB поддерживает constraints (ограничения). Если рассмотреть привычный всем constraint — `PRIMARY KEY`, то оно
работает. Но необходимо смотреть на производительность на ваших данных. Потому что это может замедлить транзакционные
механизмы.

К примеру, если использовать конструкцию `ON CONFLICT` на большом наборе вы можете получить оверхед по RAM. Используйте
аккуратно.

Документация:

- [UPDATE Statement](https://duckdb.org/docs/current/sql/statements/update)
- [Constraints](https://duckdb.org/docs/current/sql/constraints)
- [INSERT Statement](https://duckdb.org/docs/current/sql/statements/insert#on-conflict-clause)
    - [ON CONFLICT Clause](https://duckdb.org/docs/current/sql/statements/insert#on-conflict-clause)

## Быстрые `JOIN`

Быстрые `JOIN` — это один из важных аспектов при работе с данными. И у DuckDB очень быстрые `JOIN` по сравнению с
другими OLAP решениями. Быстрые `JOIN` в DuckDB — это удар в сторону ClickHouse.

Также отличительным свойством DuckDB является поддержка `ASOF JOIN`. Данный вид `JOIN`, позволяет быстро сопоставить
события, которые произошли в разное время.

Документация:

- [FROM and JOIN Clauses](https://duckdb.org/docs/current/sql/query_syntax/from)
- [AsOf Join](https://duckdb.org/docs/current/guides/sql_features/asof_join)
- [Range Joins in DuckDB](https://duckdb.org/2022/05/27/iejoin)

## Profiling (профилирование)

У DuckDB довольно богатый инструментарий для профилирования. Начиная с `EXPLAIN` и заканчивая конфигурированием
профайлинга.

Документация:

- [Profiling](https://duckdb.org/docs/current/dev/profiling)
- [DuckDB execution plan visualizer](https://db.cs.uni-tuebingen.de/explain/)

## DuckLake

DuckLake — это один из сильных ударов в сторону Apache Iceberg. Это новый формат хранения данных, который поддерживает
ACID транзакции, версионирование данных и путешествия во времени.

2026-04-13 вышла v1.0, с которой можно стартовать и изучать данный формат, подобнее
тут — [DuckLake v1.0: The Lakehouse Format Built on SQL Reaches Production-Readiness](https://ducklake.select/2026/04/13/ducklake-10/)

Более подробно про DuckLake можно узнать из
видео — [DuckLake - The SQL-Powered Lakehouse Format for the Rest of Us by Prof. Hannes Mühleisen](https://www.youtube.com/watch?v=YQEUkFWa69o)

Документация:

- [DuckLake](https://duckdb.org/docs/current/core_extensions/ducklake)
- [DuckLake v1.0: The Lakehouse Format Built on SQL Reaches Production-Readiness](https://ducklake.select/2026/04/13/ducklake-10/)
- [DuckLake - The SQL-Powered Lakehouse Format for the Rest of Us by Prof. Hannes Mühleisen](https://www.youtube.com/watch?v=YQEUkFWa69o)

## MotherDuck

MotherDuck — это облачный сервис, который позволяет использовать DuckDB в облаке. Он поддерживает все возможности
DuckDB, а также предоставляет дополнительные функции, такие как автоматическое масштабирование, управление
пользователями и интеграция с другими облачными сервисами.

Документация:

- [MotherDuck](https://motherduck.com/)

## Макросы

Макросы — это мощный инструмент, который позволяет создавать пользовательские функции и расширять функциональность
DuckDB.

Мы рассматривали интеграцию Python функций в DuckDB — [09_python_function_in_duckdb](../09_python_function_in_duckdb).
Но данный функционал может быть удобнее для некоторых кейсов.

Документация:

- [CREATE MACRO Statement](https://duckdb.org/docs/current/sql/statements/create_macro)

## DuckDB ≠ SQLite

Одно из самых частых заблуждений при изучении DuckDB — это то, что DuckDB — это просто расширенная версия SQLite.

Но это не так. DuckDB и SQLite — это два разных продукта, которые имеют разные цели и архитектуру.

DuckDB — это аналитическая база данных (OLAP), которая оптимизирована для работы с большими объемами данных

SQLite — это легковесная база данных (OLTP), которая оптимизирована для встраивания в приложения.

Документация:

- [DuckDB vs SQLite: Which Embedded Database Should You Use?](https://motherduck.com/learn/duckdb-vs-sqlite-databases/)

## MVCC

MVCC (Multi-Version Concurrency Control) — это механизм управления конкурентным доступом к данным, который позволяет
обеспечить высокую производительность и согласованность данных при работе с несколькими транзакциями одновременно.

Грубо говоря, DuckDB позволяет работать с одной базой данных нескольким процессам одновременно.

> **Но есть одно важное ограничение.**
>
> При работе с одной базой данных только один процесс может находиться в состоянии `read-write`, а все остальные могут
> быть только в состоянии `read-only`.

Документация:

- [Concurrency](https://duckdb.org/docs/current/connect/concurrency)
- [Analytics-Optimized Concurrent Transactions](https://duckdb.org/2024/10/30/analytics-optimized-concurrent-transactions)

## Benchmarks (бенчмарки)

В данном пункте нет цели доказывать, что DuckDB — это самая быстрая база данных.

Поэтому рекомендую самостоятельно изучать различные Benchmarks, которых набралось уже довольно много.

Также рекомендую провести бенчмарки на своих данных, чтобы понять, насколько DuckDB подходит для ваших задач.

Документация:

- [Benchmarks](https://duckdb.org/docs/current/guides/performance/benchmarks)
- [DuckDB vs. Polars: Performance & Memory on Massive Parquet Data](https://www.codecentric.de/en/knowledge-hub/blog/duckdb-vs-polars-performance-and-memory-with-massive-parquet-data)
- [DuckDB vs Apache Spark — The Fall of the Cluster?](https://medium.com/@mamidipaka2003/duckdb-vs-apache-spark-the-fall-of-the-cluster-c28bea3e4d38)

## DuckDB vs chDB

После того как DuckDB стал довольно популярным, многие компании начали создавать свои решения на основе DuckDB. Одним из
таких решений является chDB — это SQL OLAP движок созданный на базе ClickHouse.

Документация:

- [chDB ClickHouse site](https://clickhouse.com/docs/chdb)
- [chDB GitHub](https://github.com/chdb-io/chdb)
- [Comparing DuckDB, ChDB and Polars like a noob](https://medium.com/@MarinAgli1/comparing-duckdb-chdb-and-polars-like-a-noob-ad74584456b9)

## BI

Так как DuckDB — это OLAP-движок, то его довольно просто интегрировать в различные BI-инструменты.

После такой интеграции у вас появляется использовать все преимущества DuckDB, которые мы рассмотрели.

Документация:

- [duckdb_engine](https://pypi.org/project/duckdb-engine/)
- [Apache Superset / DuckDB](https://superset.apache.org/user-docs/databases/supported/duckdb/)
- [Modern Data Stack in a Box with DuckDB](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box#connecting-superset)

> **Полезное.**
>
> В своём
> видео [Лучший пет-проект для дата-инженера (The best pet-project for a data-engineer)](https://youtu.be/MQPHgUQvKnI)
> я уже использовал связку Metabase + DuckDB, но не делал на этом акцент.
>
> Если вы рассмотрите [Dockerfile](https://github.com/k0rsakov/pet_project_earthquake/blob/main/metabase/Dockerfile) из
> данного проекта, то вы сможете увидеть сборку Metabase + DuckDB.
>
> После сборки, вы можете запустить контейнер и подключиться к DuckDB через Metabase, чтобы визуализировать данные о
> землетрясениях.

## Встроенный менеджер секретов

В примерах ранее мы не использовали скрытия секретов, к примеру здесь:

```sql
ATTACH 'dbname=postgres user=postgres host=localhost password=postgres' AS db (TYPE postgres, SCHEMA 'public');
```

Все данные открыты, но при помощи менеджера секретов их можно спрятать на уровне БД, чтобы обращаться к ним без
указания.

Документация:

- [Secrets Manager](https://duckdb.org/docs/current/configuration/secrets_manager)
- [CREATE SECRET Statement](https://duckdb.org/docs/current/sql/statements/create_secret)
- [Securing DuckDB](https://duckdb.org/docs/current/operations_manual/securing_duckdb/overview)

Также для работы с безопасностью в DuckDB рекомендую
документацию [Securing DuckDB](https://duckdb.org/docs/current/operations_manual/securing_duckdb/overview).

## DBT + DuckDB

DuckDB отлично интегрируется с DBT, что позволяет использовать все мощности DuckDB как вычислителя. Есть отдельный пакет
[dbt-duckdb](https://github.com/duckdb/dbt-duckdb), который вы можете установить и использовать для своих трансформаций.

Документация:

- [dbt-duckdb](https://github.com/duckdb/dbt-duckdb)
- [Fully Local Data Transformation with dbt and DuckDB](https://duckdb.org/2025/04/04/dbt-duckdb)

Полезные ссылки:

- [Инфраструктура для Data-Engineer DBT](https://habr.com/ru/articles/854990/)

## Работа с гео-данными

DuckDB быстро набрал популярность в сообществе гео-данных, потому что он позволяет быстро считать большие объёмы данных.

Одним из основных моментов в популярности пакета `spatial` является то, что он по использует синтаксис PostGIS, который
уже знаком многим специалистам, работающим с гео-данными.

А если говорить ещё проще, то раньше все считали данные в PostgreSQL, потому что PostGIS — это расширение для
PostgreSQL.

А так как мы видим, что DuckDB быстрее PostgreSQL, то многие начали использовать именно DuckDB.

Документация:

- [Spatial Extension](https://duckdb.org/docs/current/core_extensions/spatial/overview)
- [Spatial Functions](https://duckdb.org/docs/current/core_extensions/spatial/functions)
- [PostGEESE? Introducing The DuckDB Spatial Extension](https://duckdb.org/2023/04/28/spatial)
- [Spatial Joins in DuckDB](https://duckdb.org/2025/08/08/spatial-joins)

## ETL/ELT/EL + DuckDB

Так как DuckDB является мощным движком для вычислений, он очень просто встраивается в различные ETL/ELT/EL пайплайны.

В своём
видео [Лучший пет-проект для дата-инженера (The best pet-project for a data-engineer)](https://youtu.be/MQPHgUQvKnI). Я
как раз использую DuckDB как удобный вычислитель, который сразу обращается к API и складывает данные в S3.

DuckDB очень просто установить как Python пакет, что мы рассмотрели в данном
примере — [04_quick_start_python](../04_quick_start_python) или использовать через Docker, что мы рассмотрели в данном
примере — [15_duckdb_containerization](../15_duckdb_containerization).

Документация:

- [Python API](https://duckdb.org/docs/current/clients/python/overview)

## Тонкости DuckDB

Данный раздел может показаться чуть больше, но тут просто хотелось бы сделать акцента на некоторые моменты, которые
могут быть полезными при работе с DuckDB.

### Отложенные вычисления

По своей природе DuckDB считает быстро, но максимально старается "_отложить_" момент расчётов и при возможности работает
с мета-данными. Это называется Late materialization (поздняя материализация).

> DuckDB uses a technique called late materialization, where data is only fetched or processed when absolutely
> necessary. In traditional
> databases, materializing data (i.e., fetching and loading full rows
> into memory) is done early in query execution, even if only a subset
> of columns is needed for the final result. DuckDB, however,
> postpones this materialization step as much as possible, working with
> metadata (e.g., column indices) rather than actual row data until it
> needs to materialize only the specific columns required for the query
> result.
> This approach minimizes unnecessary data movement and
> processing, leading to substantial performance improvements,
> especially for complex queries that involve filtering or joining large
> datasets.
>
> _DuckDB: Up and Running, Wei-Meng Lee_

Также это рассказывается в
видео [DuckDB: How to Build 100x Faster Analytics Databases (with Co-Creator Hannes Mühleisen)](https://youtu.be/pZV9FvdKmLc?si=8UV3tXjVKgwPdLb8).
Тайм-код — 1:12:57 (t4377)



















































































































