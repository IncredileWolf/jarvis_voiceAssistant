from collections import deque

from config import MAX_HISTORY


class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(self):

        self.messages = deque(
            maxlen=MAX_HISTORY,
        )

    def add(
        self,
        role,
        content,
    ):

        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )

    def build_context(self):

        context = ""

        for message in self.messages:

            context += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        return context

    def clear(self):

        self.messages.clear()