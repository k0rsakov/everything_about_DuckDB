# Использование расширений для DuckDB

Документация:

- [Extensions](https://duckdb.org/docs/current/extensions/overview)
- Списки расширений:
  - [Core Extensions](https://duckdb.org/docs/current/core_extensions/overview)
  - [List of Community Extensions](https://duckdb.org/community_extensions/list_of_extensions)

## Notes

Если рассматривать расширения из списка [Extensions](https://duckdb.org/docs/current/extensions/overview), то они все
будут устанавливаться автоматически,
подробнее — [Autoloading Extensions](https://duckdb.org/docs/current/extensions/overview#autoloading-extensions).

А расширения из [List of Community Extensions](https://duckdb.org/community_extensions/list_of_extensions) необходимо
устанавливать самостоятельно.

```bash
rm /Users/i.korsakov/.duckdb/extensions/v1.5.1/osx_arm64/tpch.duckdb_extension
```