from core.speaker import Speaker
from core.speech import SpeechRecognizer
from commands.browser import BrowserCommands
from commands.router import CommandRouter



class Assistant:
    """
    Main controller of the application.
    Coordinates all modules.
    """

    def __init__(self):
        self.speaker = Speaker()
        self.listener = SpeechRecognizer()

        self.router = CommandRouter()

        self.router.register("google", BrowserCommands.open_google)
        self.router.register("youtube", BrowserCommands.open_youtube)

    def start(self):
        """
        Starts Jarvis.
        """
        self.speaker.speak("Hello Rohit. Jarvis is online.")

        while True:

            command = self.listener.listen()

            if command is None:
                continue

            print(f"\nUser : {command}")

            if command in ["exit", "quit", "bye"]:

                self.speaker.speak("Goodbye Rohit.")

                break

            self.process_command(command)

    def process_command(self, command):

        if self.router.execute(command):
            self.speaker.speak("Done.")
        else:
            self.speaker.speak("Sorry,I don't understand that command.")