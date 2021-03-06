from interface.print import PrintClass
from interface.mainScreen import MainScreen
from database.querys import main

class Interface:
  def __init__(self, queryClass: main.MainQuerys) -> None:
    self.printClass = PrintClass()
    self.screen = MainScreen(self.printClass, queryClass)
    self.queryClass = queryClass

  def init(self):
    while True:
      self.printClass.clean_screen()
      self.printClass.print_big_name()

      print()
      print()

      print(' [1] Treinar frases ')
      print(' [2] Treinar perguntas ')
      print(' [3] Executar Query ')
      print(' [4] Adcionar conceito/tema ')
      print(' [5] Sair')

      print()

      result = input(' ')
      
      if not result.isdigit(): continue

      result = int(result)
      
      if result == 5: break

      if result > 0 and self.screen.number_of_screens >= result:
        self.screen.access(result)