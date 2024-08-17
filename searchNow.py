import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser as wb

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


query=takeCommand().lower()

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query or "search" in query:
        import wikipedia as googleScrap
        query =query.replace("orion","")
        query=query.replace("search", "")
        query=query.replace("google","")
        speak("this is what i found")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            speak(result)
        except:
            speak("sorry sir i couldn't find anyting")

def searchYoutube(query):
    if "youtube" in query or "search youtube" in query:
        
        query =query.replace("orion","")
        query=query.replace("search", "")
        query=query.replace("youtube","")
        try:
            speak("this is what i found")
            web ="https://www.youtube.com/results?search_query="+ query
            wb.open(web)
            pywhatkit.playonyt(query)
            speak("done sir ")
        except:
            speak("sorry sir i couldn't find anyting")



def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching from wikipedia")
        query =query.replace("orion","")
        query=query.replace("search", "")
        query=query.replace("wikipedia","")
        try:
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        except:
            speak("sorry sir i couldn't find anyting")
    elif "who is" in query:
        query =query.replace("orion","")
        query=query.replace("search", "")
        query=query.replace("who is", "")
        query=query.replace("wikipedia","")
        try:
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        except:
            speak("sorry sir i couldn't find anyting")







