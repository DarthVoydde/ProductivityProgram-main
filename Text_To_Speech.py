# Imports
import pyttsx3

# initialize the engine
engine = pyttsx3.init()

# define the read function take the text as a parameter
def read(text):
    # check if the user is online
    engine.say(text)
    engine.runAndWait()

read("Hello, this is a text to speech test.")
# if the user isn't online
# convert the text to text to speech using pyttsx3
# if the user is online
# convert the text to tts using a better module
