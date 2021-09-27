from utils.commands import the_command_is_an_quit
import random, time, os

class AnswerQuestionsScreen:
  def __init__(self, window) -> None:
    self.window = window
    
    self.path = os.path.abspath(__file__).replace('answerQuestionsScreen.py', '') + 'questions.txt'

    self.questions: list = self.read_all_questions()

    self.minium_size = 10

  def execute(self) -> None:    
    if len(self.questions) == 0:
      self.error('Não há perguntas para serem respondidas')
      return

    # Entrando no loop de perguntas
    while True:
      self.window.printClass.clean_screen()
      
      question = random.choice(self.questions)
      total_answers = self.window.answerQuestionsQuery.number_of_rows()

      print(f'Questão: {question}')
      print()
      print(f'Total de perguntas: {len(self.questions)}')
      print(f'Total de perguntas já respondidas: {total_answers}')
      print(f'Tamanho mínimo aceito: {self.minium_size}')

      answer = str(input(' ')).strip()

      if the_command_is_an_quit(answer):
        break

      if answer.lower() == 'add':
        self.add_question()
        continue

      if self.minium_size > len(answer):
        continue

      self.window.answerQuestionsQuery.insert(question, answer)

  def error(self, message: str, sec: int = 2) -> None:
    self.window.printClass.clean_screen()

    print(message)
    print()

    time.sleep(sec)

  def read_all_questions(self) -> list:
    with open(self.path) as src:
      questions = src.read().split('\n')

    return [q for q in questions if len(q) > 1]

  def add_question(self) -> None:
    os.system(self.path)