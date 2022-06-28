from database.querys.main import MainQuerys
from datetime import datetime
import random

class ThemeQuerys:
  def __init__(self, querys: MainQuerys) -> None:
    self._querys = querys
    self.name_table = 'themes'

  def insert(self, name: str, language_id: int) -> int:
    return self._querys.insert(self.name_table,
      f"""
        INSERT INTO {self.name_table} (name, language_id, date) VALUES 
        ('{name}', {language_id}, '{datetime.now()}')
      """
    )

  def select(self) -> list:
    return self._querys.select_all(self.name_table)

  def find_by_id(self, id: int) -> list or None:
    result = self._querys.select_with_condition(self.name_table,
    f"""
      SELECT * FROM {self.name_table} WHERE id = {id}
    """)

    if len(result) == 0: return []

    return result[0]

  def select_a_random_theme(self) -> tuple:
    size = self._querys.rows_in_a_table(self.name_table)

    id = random.choice(range(size)) + 1
    
    return self.find_by_id(id)

  def find_by_name(self, name) -> list:
    return self._querys.select_with_condition(self.name_table, 
      f"""
        SELECT * FROM {self.name_table} WHERE name = '{name}';
      """
    )




  