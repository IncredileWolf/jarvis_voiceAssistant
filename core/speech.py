import speech_recognition as sr
import logging


class SpeechRecognizer:
    """
    Handles microphone input and converts speech to text.
    """

    def __init__(self):
        self.recognizer = sr.Recognizer()

        # Makes recognition less sensitive to background noise
        self.recognizer.energy_threshold = 300
        self.recognizer.pause_threshold = 0.8
        self.recognizer.dynamic_energy_threshold = True

    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")
            logging.info("Listening...")

            # Adjust to surrounding noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

                print("🔍 Recognizing...")

                text = self.recognizer.recognize_google(audio)

                logging.info(f"Recognized: {text}")

                return text.lower()

            except sr.WaitTimeoutError:

                print("⌛ No speech detected.")

                return None

            except sr.UnknownValueError:

                print("❌ Could not understand.")

                return None

            except sr.RequestError as e:

                print("Google API Error")

                logging.error(e)

                return None