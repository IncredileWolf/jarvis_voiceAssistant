from core.logger import setup_logger
from core.assistant import Assistant


def main():

    setup_logger()

    assistant = Assistant()

    assistant.start()


if __name__ == "__main__":
    main()