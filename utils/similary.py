from utils.information import Information

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