import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open chat gpt" in c.lower():
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    elif c.lower().startswith("play"):
        song_name = c.lower().replace("play", "").strip()
        if song_name in musicLibrary.music:
            speak(f"Playing {song_name}")
            webbrowser.open(musicLibrary.music[song_name])
        else:
            speak(f"Sorry, I don't have {song_name} in my music library.")

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=1)
                print("Listening...")
                audio = r.listen(source,timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)

            if "hello" in word.lower():
                print(f"You said: {word}")  
                speak("YA")
                print("Ya")
                
                with sr.Microphone() as source:
                    print("hello is listening...")
                    audio = r.listen(source,timeout=5, phrase_time_limit=5)
                
                command = r.recognize_google(audio)
                print(f"You said: {command}")
                processCommand(command)
        
        except sr.WaitTimeoutError:
            print("No speech detected. Listening again...")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")