from database.querys import main, themes, phrases
from interface.print import PrintClass
from time import sleep
from utils.commands import the_command_is_an_quit

class Screen:
  def __init__(self, printClass: PrintClass, queryClass: main.MainQuerys) -> None:
    self.printClass = printClass
    self.number_of_screens = 3

    self.queryClass = queryClass
    self.themeQuery = themes.ThemeQuerys(queryClass)
    self.phrasesQuery = phrases.PhrasesQuerys(queryClass)

  def access(self, screen):
    screens = {
      '1': self.training,
      '2': self.query,
      '3': self.add_theme
    }

    screens[str(screen)]()
    sleep(0.2)

  def training(self):
    _type = 'Random Theme'

    while True:
      self.printClass.clean_screen()

      phrases_make_today = self.phrasesQuery.select_all_phrases_today()

      if _type == 'random':
        row_theme = self.themeQuery.select_a_random_theme()
      else:
        result = self.themeQuery.find_by_name(_type)

        if len(result) != 0: row_theme = result[0]
        else: row_theme = self.themeQuery.select_a_random_theme() 

      total_phrase = self.phrasesQuery.number_of_rows()

      print(f'Tema: {row_theme[1]}          Digite "q" para sair')
      print()
      print(f'Frases já feitas: {total_phrase}')
      print(f'Frases feitas hoje: {len(phrases_make_today)}')
      print()

      phrase = input(' ')

      # Se começar com uma interrogação, quer dizer uma prerrogativa para alteração do tema
      if phrase[0] == '?':
        _type = phrase[1:]
        continue

      if the_command_is_an_quit(phrase): break

      if len(phrase) < 5: continue
      
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

  def add_theme(self):
    self.printClass.clean_screen()

    theme = input(' - ')

    self.themeQuery.insert(theme)