from ai.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def generate(self, conversation: str):

        return (
            "Gemini integration "
            "coming soon."
        )