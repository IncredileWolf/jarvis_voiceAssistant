import requests
from config import OLLAMA_MODEL, OLLAMA_URL



class OllamaProvider:
    """
    Handles communication with the local Ollama server.
    """

    def __init__(self):
        self.url = OLLAMA_URL
        self.model = OLLAMA_MODEL

        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8"
        ) as file:

            self.system_prompt = file.read()

    def generate(self, prompt: str) -> str:
        try:
            full_prompt = f"""
            {self.system_prompt}

                Conversation History:

                User: {prompt}

                Assistant:
                """

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                },
                timeout=60,
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "Sorry, I couldn't generate a response.")

        except requests.exceptions.ConnectionError:
            return "I can't connect to Ollama. Is the Ollama server running?"

        except requests.exceptions.Timeout:
            return "Ollama took too long to respond."

        except Exception as e:
            return f"Unexpected error: {e}"