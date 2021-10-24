from datetime import datetime
from database.querys.phrases import PhrasesQuerys
import unidecode
import nltk


class WordForDay:
  def __init__(self, phrasesQuerys: PhrasesQuerys) -> None:
    self.phrasesQuerys = phrasesQuerys
    self.now = datetime.timestamp(datetime.now())

    nltk.download('averaged_perceptron_tagger')

    self._define_verbs_and_nouns()
    self.classify()


  def classify(self) -> None:
    """
      All words arranged on the day they were written.
    """
    self.phrases = self.phrasesQuerys.select_all()

    information_words = {}

    for row in self.phrases:
      phrase = row[1]

      day = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')

      for word in phrase.split():
        word = unidecode.unidecode(word.lower())

        grammatical_class = None

        if word in self.verbs:
          grammatical_class = "VB"
        # elif word in self.nouns:
        #   grammatical_class = "NN"
        else:
          continue

        if word not in information_words.keys():
          information_words[word] = {
            'frequency': 1,
            'last_day': day,
            'days': 0,
            'grammatical_class': grammatical_class
          }
        
        else:
          information_words[word]['frequency'] += 1
          information_words[word]['last_day'] = self._is_later(day, information_words[word]['last_day'])


    # Transform the date in days
    for w in information_words:
      information_words[w]['days'] = int(round((self.now - datetime.timestamp(information_words[w]['last_day']))  / 86400, 0))

    self.data = information_words

  def _define_verbs_and_nouns(self):
    texts = [unidecode.unidecode(i[1].strip()).lower() for i in self.phrasesQuerys.select_all()]

    tokenized = nltk.word_tokenize(" ".join(texts))

    self.verbs = [word for word, pos in nltk.pos_tag(tokenized) if 'VB' in pos]
    self.nouns = [word for word, pos in nltk.pos_tag(tokenized) if pos == 'NN']


  def get_words(self) -> list:
    self.classify()
    return sorted(self.data.items(), key = lambda d: d[1]['days'], reverse=True)


  def _is_later(self, date: datetime, compare: datetime) -> bool:
    if self.now - datetime.timestamp(date) < self.now - datetime.timestamp(compare):
      return date
    else:
      return compare