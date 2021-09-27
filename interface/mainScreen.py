from interface.screens.answerQuestionsScreen import AnswerQuestionsScreen
from database.querys import main, themes, phrases, answerQuestions
from interface.screens.phrasesScreen import PhrasesScreen
from interface.print import PrintClass
from time import sleep
from utils.commands import the_command_is_an_quit

class MainScreen:
  def __init__(self, printClass: PrintClass, queryClass: main.MainQuerys) -> None:
    self.printClass = printClass
    self.number_of_screens = 4

    self.queryClass = queryClass
    self.themeQuery = themes.ThemeQuerys(queryClass)
    self.phrasesQuery = phrases.PhrasesQuerys(queryClass)
    self.answerQuestionsQuery = answerQuestions.AnswerQuestionQuery(queryClass)

  def access(self, screen):
    screens = {
      '1': self.training,
      '2': self.answerQuestion,
      '3': self.query,
      '4': self.add_theme
    }

    screens[str(screen)]()
    sleep(0.2)

  def training(self):
    phrasesScreen = PhrasesScreen(self)
    phrasesScreen.execute()

  
  def answerQuestion(self):
    answerQuestionsScreen = AnswerQuestionsScreen(self)
    answerQuestionsScreen.execute()

  def query(self):
    self.printClass.clean_screen()

    while True:
      text_query = input(' - ')

      if len(text_query) == 0: continue
      
      if the_command_is_an_quit(text_query): break

      print()

      result = self.queryClass.execute_a_query(text_query)

      if len(result['return']) > 0:
        for row in result['return']:
          print(row)

      print()
      print(result['message'])

      print()
      print()


  def add_theme(self):
    self.printClass.clean_screen()

    theme = input(' - ')

    if the_command_is_an_quit(theme): return

    self.themeQuery.insert(theme)