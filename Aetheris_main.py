import pyttsx3
import speech_recognition

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold=100
        audio=r.listen(source,0,4)

    try:
        print("understanding....")
        query=r.recognize_bing(audio,language="en-in")
        print(f"you said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if "wake up" in query:
            from GreetME import greetMe
            greetMe()
            while True:
                query=takeCommand().lower
                if "go to sleep" in query:
                    speak("Ok sir !, you can call me anytime")
                    break




