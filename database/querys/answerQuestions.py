from database.querys.main import MainQuerys
from datetime import datetime

class AnswerQuestionQuery:
  def __init__(self, querys: MainQuerys) -> None:
    self._querys = querys
    self.name_table = 'answer_questions'

  def insert(self, question: str, answer: str) -> int:
    question = question.replace("'", "''")
    answer = answer.replace("'", "''")
    return self._querys.insert(self.name_table,
      f"""
        INSERT INTO {self.name_table} (answer, question, date) VALUES 
        ('{answer}', '{question}', '{datetime.now()}')
      """
    )

  def select_all(self) -> list:
    return self._querys.select_all(self.name_table)

  def number_of_rows(self) -> int:
    return self._querys.rows_in_a_table(self.name_table)



  