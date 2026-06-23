# Всё. Вообще всё про DuckDB

- ✉️ Вопросы, обучение, консультации по Data Engineering — пиши в
  личку: https://korsak0v.notion.site/Data-Engineer-185c62fdf79345eb9da9928356884ea0
- 💥 Аналог Notion (если не работает ссылка выше) — https://www.dataengineers.pro/mentors/korsakov-ivan
- [Видео](https://youtu.be/9L63L__fX0k) — https://youtu.be/9L63L__fX0k


## О видео

🔥 Что такое DuckDB и как эта база данных меняет привычные подходы к анализу и обработке данных? В этом детальном 2-часовом [руководстве](https://youtu.be/9L63L__fX0k) мы разберем DuckDB с точки зрения современной аналитики и работы с данными. Поговорим про внутреннюю архитектуру, колоночное хранение, векторизованный движок выполнения запросов, а также обсудим ключевые проблемы и их решения при обработке различных форматов.

На реальных примерах мы пройдем весь цикл работы с данными: от быстрого старта в CLI и DBeaver до интеграции движка в Python-скрипты. Научимся эффективно читать форматы `.parquet`, `.csv` и `.json`, работать со сложными схемами, использовать кастомные Python-функции и расширения, а также развернем и настроим связку DuckDB с локальным S3-хранилищем (MinIO) и СУБД PostgreSQL.

🗂️ GitHub репозиторий с кодом: https://github.com/k0rsakov/everything_about_duckdb

✉️ Вопросы, обучение, консультации по Data Engineering — пиши в личку: https://korsak0v.notion.site/Data-Engineer-185c62fdf79345eb9da9928356884ea0

💥 Аналог Notion (если не работает ссылка выше) — https://www.dataengineers.pro/mentors/korsakov-ivan

💡 В конце [видео](https://youtu.be/9L63L__fX0k) разберем готовые рецепты для продакшена, реальные возможности движка и обсудим сценарии, в которых DuckDB позволяет эффективно обрабатывать данные локально, избегая развертывания тяжелых Big Data кластеров.

Мои соцсети и полезные ссылки:
- Mentorship/консультации по Data Engineering — https://korsak0v.notion.site/Data-Engineer-185c62fdf79345eb9da9928356884ea0
- TG-канал — https://t.me/DataLikeQWERTY
- Instagram — https://www.instagram.com/i__korsakov/
- Habr — https://habr.com/ru/users/k0rsakov/publications/articles/

Таймкоды:
- 0:00 — Вступление
- 1:51 — История создания DuckDB
- 2:47 — Специфика аналитической обработки данных (OLAP)
- 5:33 — Поддержка ACID в DuckDB
- 6:21 — Внутренняя архитектура DuckDB и векторизованный движок DuckDB
- 10:34 — Реальные объемы данных в современной аналитике
- 12:34 — Резюме по теории (ACID, OLAP, OLTP, etc.)
- 15:24 — SQL для всего и его важность в DuckDB
- 17:44 — Быстрый старт DuckDB через интерфейс командной строки (CLI)
- 21:51 — Быстрый старт DuckDB в DBeaver
- 24:27 — Быстрый старт DuckDB в экосистеме Python
- 25:27 — Способы подключения (Python DuckDB connect)
- 29:56 — Чтение различных форматов файлов (Parquet, CSV, JSON)
- 38:16 — Работа с динамическими и сложными схемами данных
- 41:27 — Интеграция и работа с библиотекой Pandas
- 44:20 — Написание и запуск своих Python-функций внутри DuckDB
- 47:23 — Знакомство с экосистемой расширений в DuckDB (Extensions)
- 50:48 — Практическое применение расширений в DuckDB
- 53:20 — Прямые вызовы внешних API через SQL в DuckDB
- 55:43 — Крутые фишки и диалект современного SQL в DuckDB
- 1:02:18 — Тонкая настройка и конфигурация движка DuckDB
- 1:06:14 — Контейнеризация DuckDB. DuckDB in Docker
- 1:11:28 — Интеграция с объектным хранилищем MinIO S3
- 1:25:57 — Совместное использование DuckDB и PostgreSQL
- 1:29:23 — Разбор расширения pg_duckdb для PostgreSQL
- 1:34:45 — Интеграция с JupyterLab при помощи JupySQL
- 1:37:13 — Продвинутые возможности и готовые рецепты для продакшена
- 1:46:57 — Заключение и финальные выводы

#duckdb #dataengineering #python #sql #olap #database #docker #pandas #s3 #minio #postgresql #dataengineer #analytics #etl #bigdata

## О проекте

- [00_theory](00_theory) — Теория (История создания DuckDB, специфика OLAP, поддержка ACID, внутренняя архитектура и векторизованный движок, реальные объемы данных в современной аналитике)
- [01_sql_is_everything](01_sql_is_everything) — SQL для всего и его важность в DuckDB
- [02_quick_start_cli](02_quick_start_cli) — Быстрый старт DuckDB через интерфейс командной строки (CLI)
- [03_quick_start_dbeaver](03_quick_start_dbeaver) — Быстрый старт DuckDB в DBeaver
- [04_quick_start_python](04_quick_start_python) — Быстрый старт DuckDB в экосистеме Python
- [05_python_duckdb_connect](05_python_duckdb_connect) — Способы подключения (Python DuckDB connect)
- [06_read_diff_file_formats_duckdb](06_read_diff_file_formats_duckdb) — Чтение различных форматов файлов (`.parquet`, `.csv` и `.json`)
  - [00_theory](06_read_diff_file_formats_duckdb/00_theory) — Теория по форматам файлов
- [07_read_diff_schema](07_read_diff_schema) — Работа с динамическими и сложными схемами данных
- [08_working_with_pandas_using_duckdb](08_working_with_pandas_using_duckdb) — Интеграция и работа с библиотекой Pandas
- [09_python_function_in_duckdb](09_python_function_in_duckdb) — Написание и запуск своих Python-функций внутри DuckDB
- [10_introduction_duckdb_extensions](10_introduction_duckdb_extensions) — Знакомство с экосистемой расширений (Extensions)
- [11_using_duckdb_extension](11_using_duckdb_extension) — Практическое применение расширений DuckDB
- [12_calling_api_using_duckdb](12_calling_api_using_duckdb) — Прямые вызовы внешних API через SQL в DuckDB
- [13_sql_features_in_duckdb](13_sql_features_in_duckdb) — Крутые фишки и диалекты современного SQL в DuckDB
- [14_configuring_duckdb](14_configuring_duckdb) — Тонкая настройка и конфигурация движка DuckDB
- [15_duckdb_containerization](15_duckdb_containerization) — Контейнеризация DuckDB. DuckDB in Docker
  - [01_docker_duckdb_cli](15_duckdb_containerization/01_docker_duckdb_cli) — Запуск DuckDB CLI в Docker
  - [02_docker_duckdb_python](15_duckdb_containerization/02_docker_duckdb_python) — Использование DuckDB с Python в Docker
  - [03_docker_official_image](15_duckdb_containerization/03_docker_official_image) — Работа с официальным Docker-образом DuckDB
- [16_using_duckdb_with_minio_s3](16_using_duckdb_with_minio_s3) — Интеграция с объектным хранилищем MinIO S3
- [17_using_duckdb_with_postgresql](17_using_duckdb_with_postgresql) — Совместное использование DuckDB и PostgreSQL
- [18_using_extension_pg_duckdb](18_using_extension_pg_duckdb) — Разбор расширения `pg_duckdb` для PostgreSQL
- [19_using_jupysql_for_duckdb_in_jupyterlab](19_using_jupysql_for_duckdb_in_jupyterlab) — Интеграция с JupyterLab при помощи JupySQL
- [20_duckdb_capabilities_and_recipes](20_duckdb_capabilities_and_recipes) — Продвинутые возможности и готовые рецепты для продакшена

### Виртуальное окружение

Настройка виртуального окружения:

```bash
uv sync
```
