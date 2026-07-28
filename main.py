"""
Entry point of the Jarvis Voice Assistant.
"""

from core.assistant import Assistant


def main():
    assistant = Assistant()
    assistant.start()


if __name__ == "__main__":
    main()