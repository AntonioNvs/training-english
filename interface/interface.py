from interface.print import PrintClass
from interface.screen import Screen


class Interface:
  def __init__(self) -> None:
    self.printClass = PrintClass()
    self.screen = Screen(self.printClass)

  def init(self):
    while True:
      self.printClass.clean_screen()
      self.printClass.print_big_name()

      print()
      print()

      print(' [1] Treinar frases ')
      print(' [2] Editar assuntos ')
      print(' [3] Executar Query ')
      print(' [4] Sair')

      print()

      result = int(input(' '))

      if result == 4: break

      if result > 0 and self.screen.number_of_screens >= result:
        self.screen.access(result)