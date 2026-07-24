import logging
import pyttsx3

from config import VOICE_RATE


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", VOICE_RATE)

    def speak(self, text: str):
        try:
            logging.info("Speaking: %s", text)
            print(f"Jarvis: {text}")

            # Clear any pending speech
            self.engine.stop()

            self.engine.say(text)
            self.engine.runAndWait()

        except Exception:
            logging.exception("Error while speaking")