# История DuckDB

Полная история появления Duckdb рассказана в
видео — [DuckDB: How to Build 100x Faster Analytics Databases (with Co-Creator Hannes Mühleisen)](https://www.youtube.com/watch?v=pZV9FvdKmLc).

Что я бы выделил:

- MIT лицензия. Полностью бесплатно и открыто.
- Без инъекций
- Установка без зависимостей (не нужно ставить Java, C++, etc)
    - К примеру, вы пробовали поставить PostgreSQL из исходного кода?
- Открытое community
- Открыт к расширениям. Можно установить недостающие "*детали*" — [DuckDB Community Extensions](https://duckdb.org/2024/07/05/community-extensions)
    - Если вам необходимо работать с S3, ставите расширение `httpfs`
    - Если вам необходимо работать с GIS данными, ставите расширение `spatial`
- Взяли быстрый язык программирования C++.
- Определили чётко цель инструмента.
- Применили лучшие практики по построению БД.
- Написали всё с нуля. Исключив легаси и "*стандарты*". Сделали как нужно.
- Сделан с оглядкой на "*боли*" аналитики: дата-аналитика (data analytics), дата-инженерия (data engineering), наука о
  данных (data science).
- Сама DuckDB не получала инвестиций, чтобы ни от кого не зависеть. Но MotherDuck получила инвестиции
  на $100 млн. — [Duck and Roll: MotherDuck is Open for All With \$100M in the Nest](https://motherduck.com/blog/motherduck-open-for-all-with-series-b/)
- Недавно выпустили обзорную книгу по DuckDB — [DuckDB in Action](https://motherduck.com/duckdb-book-brief/)

#### Создатели DuckDB

- [Hannes Mühleisen](https://hannes.muehleisen.org/research/) — Co-founder & CEO of DuckDB Labs

![](https://images.fd.nl/LggoUMo6exTXO84CPChT2LvGpyU.jpg?auto=format&w=1280&q=45)

- [Mark Raasveldt](https://mytherin.github.io/) — Co-founder & CTO of DuckDB Labs

![](https://deingenieur.nl/_Resources/Persistent/e/4/a/d/e4adf090e52eaa752c676c895647efea5bbcd2cd/mark-raasveldt-robert-lagendijk-r-2022-5033-klein-850x565.jpg)
