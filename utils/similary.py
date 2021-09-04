import nltk

class Similary:
  def __init__(self, sentences) -> None:
    nltk.download('stopwords')
    self.stop_words = nltk.corpus.stopwords.words('english')

    self.frequency = {}
    self.sentences = sentences

    self.create()


  def format_sentence(self, sentence: str) -> str:
    return sentence.replace('?', '').replace('!', '').lower()

  # Definindo a frequência de palavras
  def create(self):
    for s in self.sentences:
      for w in self.format_sentence(s).split(' '):
        if w not in self.stop_words:
          try:
            self.frequency[w] += 1
          except KeyError:
            self.frequency[w] = 1

  def compare(self, sentence: str) -> int:
    frequency = 0
    words = 0

    for w in self.format_sentence(sentence).split(' '):
      if w not in self.stop_words:
        words += 1
        try:
          frequency += self.frequency[w]
        except:
          pass

    return frequency, words