from database.querys.main import MainQuerys
from datetime import datetime

class LanguagesQuerys:
  def __init__(self, querys: MainQuerys) -> None:
    self._querys = querys
    self.name_table = 'languages'

  def insert(self, name: str) -> int:
    name = name.replace("'", "''")
    return self._querys.insert(self.name_table,
      f"""
        INSERT INTO {self.name_table} (text, date, theme_id) VALUES 
        ('{name}', '{datetime.now()}');
      """
    )

  def select_all(self) -> list:
    return self._querys.select_all(self.name_table)

  def number_of_rows(self) -> int:
    return self._querys.rows_in_a_table(self.name_table)