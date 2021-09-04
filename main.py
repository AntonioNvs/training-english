from interface.interface import Interface
from database.orm.database import Database
from database.querys import main
from database.querys import phrases
# from utils.similary import Similary

database = Database()
mainQuerys = main.MainQuerys(database)
# phrasesQuerys = phrases.PhrasesQuerys(mainQuerys)

# phrases_today = phrasesQuerys.select_all_phrases_today()

# a = Similary([i[1] for i in phrases_today])

# print(a.compare('Hi my name is Antonio'))

interface = Interface(mainQuerys)

interface.init()