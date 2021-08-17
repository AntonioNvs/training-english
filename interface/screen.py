class Screen:
  def __init__(self, printClass) -> None:
    self.printClass = printClass
    self.number_of_screens = 3

  def access(self, screen):
    screens = {
      '1': self.training(),
      '2': self.edit_lectures(),
      '3': self.query()
    }

    screens[screen]()

  def training(self):
    pass

  def edit_lectures(self):
    pass

  def query(self):
    pass