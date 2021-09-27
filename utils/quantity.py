# Retorne o tamanho médio das frases de uma lista
def get_average_size(sentences: list) -> float:
  try:
    return round(sum([len(s) for s in sentences ]) / len(sentences), 3)
  except ZeroDivisionError:
    return 0