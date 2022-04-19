import os, time

from gtts import gTTS
from playsound import playsound

file = f"{os.path.dirname(os.path.abspath(__file__))}\\trash.mp3"

def text_to_speech(text: str) -> None:
  tts = gTTS(text, lang="en", tld="com")
  tts.save(file)

def play_audio() -> None:
  playsound(file)

def tts_and_play_audio(text: str):
  text_to_speech(text)
  play_audio()

if __name__ == "__main__":
  tts_and_play_audio("Hello, My name is I don't know.")
