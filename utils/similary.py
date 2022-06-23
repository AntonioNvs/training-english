import jellyfish as jf

from utils.information import Information
from unidecode import unidecode

class Similary:
  def __init__(self, information: Information) -> None:
    self.information = information

  def compare(self, sentence: str) -> tuple:
    frequency = 0
    words = 0

    for w in self.information._format_sentence(sentence).split(' '):
      if w not in self.information.stop_words:
        words += 1
        try:
          frequency += self.information.frequency[w]
        except:
          pass

    return frequency, words

def levenshtein_method(str1: str, str2: str):
  str1 = unidecode(str1.lower())
  str2 = unidecode(str2.lower())
  
  return jf.levenshtein_distance(str1, str2)