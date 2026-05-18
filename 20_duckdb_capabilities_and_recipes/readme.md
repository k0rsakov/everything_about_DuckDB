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