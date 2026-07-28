from datetime import datetime
from pathlib import Path


class ConversationLogger:

    def __init__(self):

        Path("logs").mkdir(
            exist_ok=True,
        )

        self.file = Path(
            "logs/conversation.log"
        )

    def log(
        self,
        role,
        message,
    ):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(
            self.file,
            "a",
            encoding="utf-8",
        ) as file:

            file.write(
                f"[{timestamp}] "
                f"{role}: "
                f"{message}\n"
            )