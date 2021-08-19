from code.theme.theme import get_random_theme
from time import sleep


class Screen:
  def __init__(self, printClass) -> None:
    self.printClass = printClass
    self.number_of_screens = 3

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

      print(f'Tema: {get_random_theme()}          Digite "q" para sair')
      print()

      phrase = input(' ')

      if phrase.lower() == 'q': break

  def edit_lectures(self):
    pass

  def query(self):
    pass