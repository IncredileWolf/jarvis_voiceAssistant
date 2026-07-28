from core.logger import get_logger

logger = get_logger(__name__)


class Speaker:
    """
    Handles speech output.
    """

    def __init__(self):
        pass

    def speak(self, text: str):
        logger.info("Jarvis: %s", text)
        print(f"\n🤖 Jarvis: {text}")