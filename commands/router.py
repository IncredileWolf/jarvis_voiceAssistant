class CommandRouter:
    """
    Routes commands to registered handlers.
    Supports multiple handlers for the same keyword.
    """

    def __init__(self):
        self.commands = {}

    def register(self, keyword: str, handler):

        keyword = keyword.lower()

        if keyword not in self.commands:
            self.commands[keyword] = []

        self.commands[keyword].append(handler)

    def execute(self, command: str):

        command = command.lower()

        for keyword, handlers in self.commands.items():

            if keyword in command:

                for handler in handlers:

                    try:

                        response = handler(command)

                        if response:
                            return response

                    except Exception as e:
                        print(e)

        return None