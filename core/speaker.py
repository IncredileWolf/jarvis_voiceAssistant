import pyttsx3
import logging


class Speaker:
    """
    Handles all text-to-speech functionality.
    """

    def __init__(self, rate: int = 170):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", rate)

        voices = self.engine.getProperty("voices")

        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text: str):

        try:
            logging.info(f"Speaking : {text}")

            print(f"Jarvis : {text}")

            self.engine.say(text)

            self.engine.runAndWait()

        except Exception as e:
            logging.error(e)