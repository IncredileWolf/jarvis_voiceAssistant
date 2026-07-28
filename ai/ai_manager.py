# from ai.ollama_provider import OllamaProvider
from ai.provider_factory import ProviderFactory
from memory.conversation import ConversationMemory
from memory.logger import ConversationLogger


class AIManager:
    """
    Handles all AI interactions.
    """

    def __init__(self):

        self.provider = ProviderFactory.create()

        self.memory = ConversationMemory()

        self.logger = ConversationLogger()

    def ask(self, prompt: str):

        # Save user message
        self.memory.add(
            "user",
            prompt,
        )

        self.logger.log(
            "User",
            prompt,
        )

        # Build conversation
        context = self.memory.build_context()

        # Generate response
        response = self.provider.generate(context)

        # Save assistant response
        self.memory.add(
            "assistant",
            response,
        )

        self.logger.log(
            "Jarvis",
            response,
        )

        return response