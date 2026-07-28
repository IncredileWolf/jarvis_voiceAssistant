import webbrowser

from data.websites import WEBSITES


class WebsiteCommands:

    @staticmethod
    def open_website(command):

        command = command.lower()

        for name, url in WEBSITES.items():

            if name in command:

                webbrowser.open(url)

                return f"Opening {name}."

        return None