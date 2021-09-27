from utils.similary import Similary
from utils.commands import the_command_is_an_quit
from utils.quantity import get_average_size
import random, time

class PhrasesScreen:
  def __init__(self, window) -> None:
    self.window = window

    self._theme = 'Random Theme'
    self._type = 1
    self.phrases_make_today = self.window.phrasesQuery.select_all_phrases_today()
    self.all_phrases = [r[1] for r in self.window.phrasesQuery.select_all()]

  def execute(self) -> None:
    frequency = 0

    while True:
      self.window.printClass.clean_screen()

      # Selecionando o tema de acordo com o tipo desejado
      if self._theme == 'random':
        row_theme = self.window.themeQuery.select_a_random_theme()
      else:
        result = self.window.themeQuery.find_by_name(self._theme)

        if len(result) != 0: row_theme = result[0]
        else:
          self.error('Esse tema não existe.')
          self._theme = 'Random Theme'
          continue

      total_phrases = self.window.phrasesQuery.number_of_rows()

      print(f'Tema: {row_theme[1]}')
      print()
      print(f'Frases já feitas: {total_phrases}')
      print(f'Frases feitas hoje: {len(self.phrases_make_today)}')
      print(f'Índice frequência da última frase: {frequency}')
      print(f'Média de tamanho das frases hoje: {get_average_size(self.phrases_make_today)}')
      print()

      if self._type == 1:
        pass
        
      elif self._type == 2:
        threshold = 70
        phrase_of_context = self.select_a_context_phrase(threshold)
        print(f'Contexto: {phrase_of_context}')
        print()

      else:
        self.error('Esse tipo não existe. Colocando tipo 1.')
        self._type = 1

      phrase = input(' ')

      # Se começar com uma interrogação, quer dizer uma prerrogativa para alteração do do tema ou do tipo
      if phrase[0] == '?':
        values = phrase.split(' ')

        if len(values) > 1:
          values = values[1:]

          if values[0] == 'change_theme':
            self._theme = " ".join(values[1:])
          
          elif values[0] == 'change_type':
            try:
              self._type = int(values[1])
            except:
              self.error('Insira um tipo númerico.', 2)

        continue

      if the_command_is_an_quit(phrase): break

      if len(phrase) < 5: continue
      
      self.window.phrasesQuery.insert(phrase, int(row_theme[0]))
      self.phrases_make_today.append(phrase)

      frequency = self.compare(self.all_phrases, phrase)


  def select_a_context_phrase(self, threshold: int) -> str:
    all_row_phrases = self.window.phrasesQuery.select_all()

    all_phrases_selected = [p[1] for p in all_row_phrases if len(p[1]) >= threshold]

    return random.choice(all_phrases_selected)


  def compare(self, list_of_sentences: list, sentence: str) -> int:
    self.similary = Similary(list_of_sentences)

    x, y = self.similary.compare(sentence)

    return round(x / y, 3)

  
  def error(self, message: str, sec: int = 2) -> None:
    self.window.printClass.clean_screen()

    print(message)
    print()

    time.sleep(sec)