# Imports
import queue
import pyttsx3
import threading

# initialize the engine
engine = pyttsx3.init()
speech_queue = queue.Queue()

def speech_worker():
    while True:
        text = speech_queue.get()
        if text is None:  # Sentinel value to stop the thread
            break

        engine.say(text)
        engine.runAndWait()

threading.Thread(target=speech_worker, daemon=True).start()
# define the read function take the text as a parameter
def _read(text):
    speech_queue.put(text)
    

#Test, remove when done    
text = ("Hello, balls")

_read(text)
input("Press enter to exit")
