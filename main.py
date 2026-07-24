from core.logger import setup_logger
from core.speaker import Speaker
from core.speech import SpeechRecognizer


def main():

    setup_logger()

    speaker = Speaker()

    listener = SpeechRecognizer()

    speaker.speak("Hello Rohit. Jarvis is ready.")

    while True:

        text = listener.listen()

        if text:

            print(f"\nYou said : {text}")

            if text == "exit":

                speaker.speak("Goodbye!")

                break


if __name__ == "__main__":
    main()