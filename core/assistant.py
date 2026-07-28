from ai.ai_manager import AIManager
from commands.application import ApplicationCommands
from commands.browser import BrowserCommands
from commands.router import CommandRouter
from commands.search import SearchCommands
from commands.website import WebsiteCommands
from config import ASSISTANT_NAME, USER_NAME
from core.speaker import Speaker
from core.speech import SpeechRecognizer


class Assistant:
    """
    Main controller of the application.
    Coordinates all modules.
    """

    def __init__(self):
        self.speaker = Speaker()
        self.listener = SpeechRecognizer()
        self.ai = AIManager()

        # Initialize command router
        self.router = CommandRouter()

        # -----------------------------
        # Application Commands
        # -----------------------------
        self.router.register("open", ApplicationCommands.open_application)
        self.router.register("launch", ApplicationCommands.open_application)
        self.router.register("start", ApplicationCommands.open_application)

        # -----------------------------
        # Website Commands
        # -----------------------------
        self.router.register("open", WebsiteCommands.open_website)

        # -----------------------------
        # Browser Commands
        # -----------------------------
        self.router.register("google", BrowserCommands.open_google)
        self.router.register("youtube", BrowserCommands.open_youtube)

        # -----------------------------
        # Search Commands
        # -----------------------------
        self.router.register("search", SearchCommands.google_search)

    def start(self):
        """
        Starts Jarvis.
        """

        self.speaker.speak(
            f"Hello {USER_NAME}. {ASSISTANT_NAME} is online."
        )

        while True:

            command = self.listener.listen()

            if command is None:
                continue

            command = command.lower().strip()

            print(f"\n👤 User: {command}")

            # Exit commands
            if command in ["exit", "quit", "bye"]:

                self.speaker.speak(
                    f"Goodbye {USER_NAME}."
                )

                break

            self.process_command(command)

    def process_command(self, command):
        """
        Process the user's command.
        """

        response = self.router.execute(command)

        if response:
            self.speaker.speak(response)
            return

        # Fallback to AI
        ai_response = self.ai.ask(command)
        self.speaker.speak(ai_response)