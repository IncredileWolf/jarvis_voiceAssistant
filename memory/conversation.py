from collections import deque


class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(self, max_messages=10):
        self.messages = deque(maxlen=max_messages)

    def add(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content
        })

    def build_context(self) -> str:
        """
        Converts conversation history into a prompt.
        """

        context = ""

        for message in self.messages:
            role = message["role"].capitalize()
            context += f"{role}: {message['content']}\n"

        return context

    def clear(self):
        self.messages.clear()