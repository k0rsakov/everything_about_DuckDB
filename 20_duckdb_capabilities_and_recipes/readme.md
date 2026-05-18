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