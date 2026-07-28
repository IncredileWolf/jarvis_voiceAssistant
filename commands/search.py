import webbrowser
import urllib.parse


class SearchCommands:

    @staticmethod
    def google_search(command):

        command = command.lower()

        if not command.startswith("search"):
            return None

        query = command.replace("search", "", 1).strip()

        if not query:
            return "What would you like me to search?"

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Google for {query}."