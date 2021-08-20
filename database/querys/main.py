from database.orm.database import Database

class MainQuerys:
  def __init__(self, database: Database) -> None:
    self.database = database

  def _list_tables(self) -> list:
    names = self.database.select_table(
      f"""
        SELECT name FROM sqlite_master WHERE type='table'
      """
    )
    # Listando o nome de todas as tabelas
    return [n[0] for n in names]

  def _table_exists(self, table: str) -> None:
    if table not in self._list_tables():
      Exception(f'Does not exist a name of table like: {table}')

  def select_all(self, table: str) -> list:
    self._table_exists(table)

    return self.database.select_table(
      f"""
        SELECT * FROM {table}
      """
    )

  def select_with_condition(self, table: str, query: str) -> list:
    self._table_exists(table)

    return self.database.select_table(
      query
    )

  def insert(self, table, query) -> int:
    self._table_exists(table)

    return self.database.insert_in_table(query)

  def rows_in_a_table(self, table: str) -> int:
    self._table_exists(table)

    size = self.database.select_table(
      f"""SELECT COUNT(*) FROM {table}"""
    )

    return size[0][0]

  def execute_a_query(self, query: str) -> dict:
    return self.database.execute_command(query)