from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base class for all AI providers.
    """

    @abstractmethod
    def generate(self, conversation: str) -> str:
        pass