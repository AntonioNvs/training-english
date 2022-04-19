from database.querys.phrases import PhrasesQuerys
import nltk

class Information(PhrasesQuerys):
  def __init__(self, mainQuerys) -> None:
    super().__init__(mainQuerys)

    nltk.download('stopwords')
    self.stop_words = nltk.corpus.stopwords.words('english')

    self.frequency = {}
    self.sentences = self.select_all()

  def _format_sentence(self, sentence: str) -> str:
    return sentence.replace('?', '').replace('!', '').lower().strip()

  # Definindo a frequência de palavras
  def frequency_of_words(self) -> None:
    for s in self.sentences:
      for w in self._format_sentence(s[1]).split(' '):
        if w not in self.stop_words:
          try:
            self.frequency[w] += 1
          except KeyError:
            self.frequency[w] = 1

    