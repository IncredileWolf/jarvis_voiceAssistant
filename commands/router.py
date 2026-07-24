class CommandRouter:

    def __init__(self):
        self.commands = {}

    def register(self, keyword, handler):
        self.commands[keyword] = handler

    def execute(self, command):

        command = command.lower()

        for keyword, handler in self.commands.items():

            if keyword in command:
                return handler(command)

        return None