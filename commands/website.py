import webbrowser

from data.websites import WEBSITES


class WebsiteCommands:

    @staticmethod
    def open_website(command):

        command = command.lower()

        for website, url in WEBSITES.items():

            if website in command:

                webbrowser.open(url)

                return f"Opening {website.title()}."

        return None