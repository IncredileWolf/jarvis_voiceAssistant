"""
Application Configuration
"""

# ==========================
# Assistant
# ==========================

ASSISTANT_NAME = "Jarvis"
USER_NAME = "Rohit"

# ==========================
# Speech Recognition
# ==========================

LISTEN_TIMEOUT = 5
PHRASE_TIME_LIMIT = 8
AMBIENT_DURATION = 1

# ==========================
# Ollama
# ==========================

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:3b"

# ==========================
# Conversation
# ==========================

MAX_HISTORY = 10

# ==========================
# Logging
# ==========================

LOG_LEVEL = "INFO"

# ==========================
# Browser
# ==========================

DEFAULT_SEARCH_ENGINE = "google"