import webbrowser

class BrowserCommands:

    @staticmethod
    def  open_google(command):

        webbrowser.open("https://www.google.com")

        return True

    @staticmethod
    def open_youtube(command):

        webbrowser.open("https://www.youtube.com")

        return True