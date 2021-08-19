import os, random

current_path = os.path.abspath(__file__).replace('\\theme.py', '')

def get_themes():
  with open(f'{current_path}\\theme.txt', 'r') as src:
    themes = src.read().split()

    return [th for th in themes if th != '\n']

def get_random_theme():
    return random.choice(get_themes())

def set_theme(theme: str):
  themes = get_themes()

  # Se for vazio, retorne
  if theme == '': return

  themes.append(theme)

  with open(f'{current_path}\\theme.txt', 'w') as src:
    for th in themes:
      src.write(f'{th}\n')

