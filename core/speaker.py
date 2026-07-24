import logging
import pyttsx3

from config import VOICE_RATE

class Speaker:

    def speak(self, text: str):

        logging.info("Jarvis: %s", text)

        print(f"\n🤖 Jarvis : {text}")