from core.logger import setup_logger
from core.speaker import Speaker

def main():

    setup_logger()
    speaker = Speaker()
    speaker.speak("Hello, I am Jarvis, your voice assistant. How can I help you today?")

if __name__ == "__main__":
    main()