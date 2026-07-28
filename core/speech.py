import speech_recognition as sr

from config import (
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT,
    AMBIENT_DURATION,
)

from core.logger import get_logger

logger = get_logger(__name__)


class SpeechRecognizer:
    """
    Handles microphone input and speech recognition.
    """

    def __init__(self):

        self.recognizer = sr.Recognizer()

    def listen(self):

        try:

            with sr.Microphone() as source:

                print("\n🎤 Listening...")

                logger.info("Listening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=AMBIENT_DURATION,
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT,
                )

            print("🔍 Recognizing...")

            command = self.recognizer.recognize_google(audio)

            logger.info("Recognized: %s", command)

            return command.lower()

        except sr.WaitTimeoutError:

            print("⌛ No speech detected.")

            return None

        except sr.UnknownValueError:

            print("❌ Could not understand.")

            return None

        except sr.RequestError:

            print("❌ Google Speech API unavailable.")

            return None

        except Exception as e:

            logger.exception(e)

            return None
        