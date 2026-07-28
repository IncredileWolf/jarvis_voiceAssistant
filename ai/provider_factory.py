from config import AI_PROVIDER

from ai.ollama_provider import OllamaProvider
from ai.gemini_provider import GeminiProvider


class ProviderFactory:

    @staticmethod
    def create():

        provider = AI_PROVIDER.lower()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unknown AI provider: {provider}"
        )