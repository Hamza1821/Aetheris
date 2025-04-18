import os
import pyautogui
import pyttsx3
import webbrowser
from time import sleep

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={"comandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code" }

def openappweb(query):
    speak("launching sir")
    if ".com" in query or ".co.in" in query or ".org" in query or ".in" in query:
        query=query.replace("orion","")
        query=query.replace("open","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://{query}")
    else:
        keys=list(dictapp.keys())
        for key in keys:
            if key in query:
                os.system(f"start {dictapp[key]}")

def closeappweb(query):
    query=query.replace("orion","")
    query=query.replace("close","")
    query=query.replace("shut","")
    query=query.replace(" ","")
    speak("closing sir")
    if "one tab" in query  or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("tab closed sir")
        
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("2 tabs closed sir")
        
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("3 tabs closed sir")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("4 tabs closed sir")
       
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("5 tabs closed sir")

    else:
        keys=list(dictapp.keys())
        for key in keys:
            if key in query:
                os.system(f"taskkill /f /im {dictapp[key]}.exe")
        