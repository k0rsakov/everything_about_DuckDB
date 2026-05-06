# Расширения для DuckDB

Документация:

- [Extensions](https://duckdb.org/docs/current/extensions/overview)
- [List of Community Extensions](https://duckdb.org/community_extensions/list_of_extensions)

## Notes

В DuckDB существует нативная команда `INSTALL extension` для установки расширений, но не существует команды `UNINSTALL
extension`. Поэтому для удаления расширения необходимо удалить файл расширения вручную.

В репозитории DuckDB есть обсуждение по поводу добавления команды `UNINSTALL extension`:
- [UNINSTALL extension #16566](https://github.com/duckdb/duckdb/discussions/16566)

Команда для удаления расширения:

```bash
rm /Users/i.korsakov/.duckdb/extensions/v1.5.1/osx_arm64/airport.duckdb_extension 
```