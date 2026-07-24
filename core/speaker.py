import pyttsx3
import logging

from config import VOICE_RATE

class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", VOICE_RATE)
        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text :str):
        try :
            logging.info(f"Speaking: {text}")
            print(f"Jarvis: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logging.error(f"Error in speaking: {e}")