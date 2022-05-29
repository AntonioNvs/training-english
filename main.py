import os, atexit

from interface.interface import Interface
from database.orm.database import Database
from database.querys import main
from database.querys import phrases
from utils import analysis

database = Database()
mainQuerys = main.MainQuerys(database)

interface = Interface(mainQuerys)

def pause():
  os.system("pause")

# atexit.register(pause)
interface.init()
