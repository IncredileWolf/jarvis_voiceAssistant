import webbrowser
import urllib.parse


class SearchCommands:

    @staticmethod
    def google_search(command):

        query = command.lower().replace("search", "").strip()

        if not query:
            return "What should I search for?"

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Google for {query}."