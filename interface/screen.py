from database.querys import main, themes, phrases
from time import sleep


class Screen:
  def __init__(self, printClass, queryClass: main.MainQuerys) -> None:
    self.printClass = printClass
    self.number_of_screens = 3

    self.themeQuery = themes.ThemeQuerys(queryClass)
    self.phrasesQuery = phrases.PhrasesQuerys(queryClass)

  def access(self, screen):
    screens = {
      '1': self.training,
      '2': self.edit_lectures,
      '3': self.query
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

  def edit_lectures(self):
    pass

  def query(self):
    pass