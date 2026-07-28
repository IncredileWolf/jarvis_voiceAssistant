from ai.ollama_provider import OllamaProvider
from memory.conversation import ConversationMemory
from memory.logger import ConversationLogger
from config import USER_ROLE,ASSISTANT_ROLE

class AIManager:
    """
    Manages AI interactions, conversation memory, and logging.
    """

    def __init__(self):
        self.provider = OllamaProvider()
        self.memory = ConversationMemory()
        self.logger = ConversationLogger()

    def ask(self, prompt: str):

        # Log and store user message
        self.memory.add("user", prompt)
        self.logger.log("User", prompt)

        # Build conversation context
        context = self.memory.build_context()

        # Get AI response
        response = self.provider.generate(context)

        # Log and store assistant response
        self.memory.add("assistant", response)
        self.logger.log(USER_ROLE,prompt)
        self.logger.log(ASSISTANT_ROLE, response)

        return response