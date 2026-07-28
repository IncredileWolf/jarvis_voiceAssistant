class CommandRouter:
    """
    Routes commands to registered handlers.
    """

    def __init__(self):
        self.commands = {}

    def register(self, keyword, handler):
        keyword = keyword.lower()

        if keyword not in self.commands:
            self.commands[keyword] = []

        self.commands[keyword].append(handler)

    def execute(self, command):

        command = command.lower()

        for keyword, handlers in self.commands.items():

            if keyword in command:

                for handler in handlers:

                    response = handler(command)

                    if response:
                        return response

        return None