from database.querys import main, themes, phrases
from interface.print import PrintClass
from time import sleep
from utils.commands import the_command_is_an_quit

class Screen:
  def __init__(self, printClass: PrintClass, queryClass: main.MainQuerys) -> None:
    self.printClass = printClass
    self.number_of_screens = 2

    self.queryClass = queryClass
    self.themeQuery = themes.ThemeQuerys(queryClass)
    self.phrasesQuery = phrases.PhrasesQuerys(queryClass)

  def access(self, screen):
    screens = {
      '1': self.training,
      '2': self.query
    }

    screens[str(screen)]()
    sleep(0.2)

  def training(self):
    while True:
      self.printClass.clean_screen()

      row_theme = self.themeQuery.select_a_random_theme()

      total_phrase = self.phrasesQuery.number_of_rows()

      print(f'Tema: {row_theme[1]}          Digite "q" para sair')
      print()
      print(f'Frases já feitas: {total_phrase}')
      print()

      phrase = input(' ')

      if phrase.lower() == 'q': break

      self.phrasesQuery.insert(phrase, int(row_theme[0]))

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