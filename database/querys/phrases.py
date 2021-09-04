from database.querys.main import MainQuerys
from datetime import datetime

class PhrasesQuerys:
  def __init__(self, querys: MainQuerys) -> None:
    self._querys = querys
    self.name_table = 'phrases'

  def insert(self, name: str, theme_id: int) -> int:
    name = name.replace("'", "''")
    return self._querys.insert(self.name_table,
      f"""
        INSERT INTO {self.name_table} (text, date, theme_id) VALUES 
        ('{name}', '{datetime.now()}', '{theme_id}')
      """
    )

  def select_all(self) -> list:
    return self._querys.select_all(self.name_table)

  def number_of_rows(self) -> int:
    return self._querys.rows_in_a_table(self.name_table)

  def select_all_phrases_today(self) -> list:
    result = self.select_all()
    
    current_day = []

    for row in result:
      current_date = datetime.now()
      date = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')

      if date.year == current_date.year and date.month == current_date.month and date.day == current_date.day:
        current_day.append(row)

    return current_day



  