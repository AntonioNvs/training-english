# Retorne o tamanho médio das frases de uma lista
def get_average_size(sentences: list) -> float:
  try:
    return round(sum([len(s) for s in sentences ]) / len(sentences), 3)
  except ZeroDivisionError:
    return 0

def number_of_character(sentences: list) -> int:
  return sum([len(s) for s in sentences])