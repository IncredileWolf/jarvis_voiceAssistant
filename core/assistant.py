from ai.ai_manager import AIManager

from commands.application import ApplicationCommands
from commands.browser import BrowserCommands
from commands.router import CommandRouter
from commands.search import SearchCommands
from commands.website import WebsiteCommands

from config import (
    ASSISTANT_NAME,
    USER_NAME,
)

from core.logger import get_logger
from core.speaker import Speaker
from core.speech import SpeechRecognizer

logger = get_logger(__name__)


class Assistant:
    """
    Main controller of Jarvis.
    """

    def __init__(self):

        self.speaker = Speaker()
        self.listener = SpeechRecognizer()
        self.ai = AIManager()

        self.router = CommandRouter()

        self._register_commands()

    def _register_commands(self):

        # Application commands
        self.router.register(
            "open",
            ApplicationCommands.open_application,
        )

        self.router.register(
            "launch",
            ApplicationCommands.open_application,
        )

        self.router.register(
            "start",
            ApplicationCommands.open_application,
        )

        # Website commands
        self.router.register(
            "open",
            WebsiteCommands.open_website,
        )

        # Browser shortcuts
        self.router.register(
            "google",
            BrowserCommands.open_google,
        )

        self.router.register(
            "youtube",
            BrowserCommands.open_youtube,
        )

        # Search
        self.router.register(
            "search",
            SearchCommands.google_search,
        )

    def start(self):

        self.speaker.speak(
            f"Hello {USER_NAME}. {ASSISTANT_NAME} is online."
        )

        while True:

            command = self.listener.listen()

            if not command:
                continue

            print(f"\n👤 User: {command}")

            if command in (
                "exit",
                "quit",
                "bye",
            ):

                self.speaker.speak(
                    f"Goodbye {USER_NAME}."
                )

                break

            self.process_command(command)

    def process_command(self, command):

        try:

            response = self.router.execute(command)

            if response:

                self.speaker.speak(response)

                return

            ai_response = self.ai.ask(command)

            self.speaker.speak(ai_response)

        except Exception as e:

            logger.exception(e)

            self.speaker.speak(
                "Sorry, something went wrong."
            )