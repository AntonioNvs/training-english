from interface.interface import Interface
from database.orm.database import Database
from database.querys import main

database = Database()
mainQuerys = main.MainQuerys(database)

interface = Interface(mainQuerys)

interface.init()