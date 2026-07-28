from ai.base_provider import BaseProvider

import requests

from config import (
    OLLAMA_MODEL,
    OLLAMA_URL,
)

class OllamaProvider(BaseProvider):
    """
    Handles communication with the local Ollama server.
    """

    def __init__(self):

        self.url = OLLAMA_URL
        self.model = OLLAMA_MODEL

        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8",
        ) as file:

            self.system_prompt = file.read()

    def generate(self, conversation: str):

        full_prompt = f"""
{self.system_prompt}

Below is the conversation so far.

{conversation}

Respond as Jarvis.

Assistant:
"""

        try:

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                },
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

            return data.get(
                "response",
                "Sorry, I couldn't generate a response.",
            )

        except requests.exceptions.ConnectionError:

            return (
                "I can't connect to Ollama."
                " Is the server running?"
            )

        except requests.exceptions.Timeout:

            return "Ollama took too long to respond."

        except Exception as e:

            return f"Unexpected error: {e}"