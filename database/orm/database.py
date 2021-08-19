import sqlite3
import os

class Database:
  def __init__(self):
    self.path_database = os.path.abspath(__file__).replace('\\database.py', '') + 'database.db'

    self.create_init_tables()
    self.close_database()

  def create_init_tables(self) -> None:
    self.open_database_and_init_cursor()

    self.cursor.execute(
      """
      """)

  def open_database_and_init_cursor(self):
    self.conn: sqlite3.Connection = sqlite3.connect(self.path_database)
    self.cursor = self.conn.cursor()

  def close_database(self):
    self.cursor.close()
    self.conn.close()

  def execute_command(self, command: str):
    self.open_database_and_init_cursor()

    self.cursor.execute(command)

    self.conn.commit()

    self.close_database()

  def insert_in_table(self, command: str) -> int:
    self.open_database_and_init_cursor()

    self.cursor.execute(command)

    self.conn.commit()

    last_id = self.cursor.lastrowid

    self.close_database()

    return last_id

  def select_table(self, command) -> list:
    self.open_database_and_init_cursor()

    self.cursor.execute(command)

    rows = []
    for row in self.cursor.fetchall():
      rows.append(row)

    self.close_database()

    return rows