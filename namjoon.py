import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def introduction():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning mam, My name is Jarvis, How may I help you?")
    elif hour >=12 and hour<=18:
        speak("Good Afternoon mam, My name is Jarvis, How may I help you?")
    else :
        speak(" Hello mam, My name is Jarvis, How may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("say again..")
        return"None"
    return query

def services():
    speak("are you looking for something else")
    query = takeCommand().lower()
    if "yes" in query:
        speak("please tell me")
        moreCommands()
    

def moreCommands():
    query = takeCommand().lower()
    if 'what' in query:
        speak('Serching web for you')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"mam, the time is {strTime}")
    elif 'open google' in query:
        webbrowser.open("www.google.com")
    elif 'search' or 'google' in query:
        kit.search(query)
    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
    elif 'play' in query:
        kit.playonyt(query)
    #elif 'i am not feeling well' or 'i am sad' or 'make my mood' or ' make me happy' or 'tell me something good' in   query:


if __name__ == "__main__":
    introduction()
    if 1:
        moreCommands()

    services()    


    