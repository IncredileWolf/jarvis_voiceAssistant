import webbrowser


class BrowserCommands:

    @staticmethod
    def open_google(command=None):

        webbrowser.open("https://www.google.com")

        return "Opening Google."

    @staticmethod
    def open_youtube(command=None):

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube."