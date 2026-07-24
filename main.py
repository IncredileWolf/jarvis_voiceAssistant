from config import VOICE_RATE
from core.speaker import Speaker
import logging


def main():

    speaker = Speaker(rate=VOICE_RATE)

    speaker.speak("Hello Rohit")

    speaker.speak("Welcome to Jarvis version two.")

    speaker.speak("Let's build something amazing.")


if __name__ == "__main__":
    main()