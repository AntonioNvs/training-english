import os, time
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound

file = f"{os.path.dirname(os.path.abspath(__file__))}\\trash.mp3"

def text_to_speech(text: str) -> None:
  tts = gTTS(text, lang="en", tld="com")
  tts.save(file)


def speech_to_text() -> str:
  r = sr.Recognizer()

  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

  try:
    return r.recognize_google(audio)
  except:
    return "Doesn't possible to recognize the audio."


def play_audio() -> None:
  playsound(file)

def tts_and_play_audio(text: str):
  text_to_speech(text)
  play_audio()
  os.remove(file)

if __name__ == "__main__":
  speech_to_text()
