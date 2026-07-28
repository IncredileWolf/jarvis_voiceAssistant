import logging

logging.basicConfig(level=logging.INFO)


class Speaker:

    def speak(self, text: str):
        logging.info("Jarvis: %s", text)
        print(f"\n🤖 Jarvis: {text}")