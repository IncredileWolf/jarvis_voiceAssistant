from pathlib import Path
from datetime import datetime


class ConversationLogger:

    def __init__(self):
        self.file = Path("logs/conversation.log")
        self.file.parent.mkdir(exist_ok=True)

    def log(self, role, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.file, "a", encoding="utf-8") as f:
            f.write(
                f"[{timestamp}] {role}: {message}\n"
            )