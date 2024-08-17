import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",200)

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
        query=r.recognize_google(audio,language="en-in")
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
                query=takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir !, you can call me anytime")
                    break
                elif "hello" in query:
                    speak("hello sir. how are you?")
                    continue
                elif "hey"in query:
                    speak("yes sir")
                elif "i am fine" in query :
                    speak("thats great sir!")
                    continue
                elif "how are you" in query or "how r u" in query:
                    speak("i am all good sir!")
                elif "are you awake" in query:
                    speak("yes sir , anytime for you")
                    continue
                elif "thank you" in query or "thank u" in query:
                    speak("you are welcome sir")
                    continue
                elif "introduce yourself" in query or "who are you" in query:
                    speak("i am orion, the personal assistant of sir Hamza Mubin ")
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query or "who is" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)  
                elif "temperature" in query:
                    url=f"https://www.google.com/search?q={query}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div", class_= "BNeawe").text
                    speak(f"the temperature is {temp}")
                elif "shutdown" in query:
                    speak("shutting down ! see you later sir")
                    exit();
                


                else:
                    continue
        
        else:
            continue




