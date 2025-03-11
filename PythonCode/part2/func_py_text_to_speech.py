# func_py_text_to_speech.py
import pyttsx3

def func_py_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

func_py_text_to_speech("Hello, this is a text-to-speech test!")
