# Imports
import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init()
    # Adjust the speed of the TTS voice. 
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def _read(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()