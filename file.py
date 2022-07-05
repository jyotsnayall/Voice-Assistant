import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes


# Listen to Microphone & return the audio as text using google
def transform():
    r = sr.Recognizer();
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.8
        said = r.listen(source)
        
        try:
            print("I am listening")
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry, I did not understand")
            print("I am waiting")
        except sr.RequestError:
            print("Sorry, the service is down")
            print("I am waiting")
        except:
            print("I am waiting")


def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


# engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#     print(voice)


# Return the weekday name
def query_day():
    date = datetime.date.today()
    #print(date)
    weekday = date.weekday()
    #print(weekday)
    mapping = {
        0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        print(f"Today is {mapping[weekday]}")
        speaking(f"Today is {mapping[weekday]}")
    except:
        pass


# Returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(f"It's {time[0:2]}:{time[3:5]} right now")
    speaking(f"It's {time[0:2]} {time[3:5]} right now")


# Intro greeting at startup
def whatsup():
    speaking('''Hey, my name is Ganky. I'm your personal assistant.
    How may I help you?
    ''')


# The Heart of Assistant. dont break </3. Takes queries & returns answers. Very smart. Toddler
def querying():
    whatsup()
    start = True
    while(start):
        q = transform().lower()
        
        if "who are you" in q:
            whatsup()
            continue
        
        elif "your name" in q:
            speaking("I'm Ganky. Your Virtual Assistant")
            continue
            
        elif "youtube" in q:
            speaking("Opening YouTube")
            webbrowser.open('https://www.youtube.com/')
            continue
        elif "browser" in q:
            speaking("Opening Web Browser")
            webbrowser.open('https://www.google.com/')
            continue  
            
        elif "what day" in q:
            query_day()
            continue
        elif "what time" in q:
            query_time()
            continue
            
        elif "shutdown" in q:
            print("Shutting down")
            speaking("Shutting down")
            break
            
        elif "wikipedia" in q:
            speaking("Checking wikipedia")
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences=2)
            speaking("Found on wikipedia")
            speaking(result)
            continue
        
        elif "search" in q:
            speaking("Searching on google")
            pywhatkit.search(q)
            speaking("This is what I found")
            continue
        
        elif "joke" in q:
            speaking(pyjokes.get_joke())
            continue
            
        elif "play" in q:
            speaking(f"playing {q}")
            pywhatkit.playonyt(q)
            continue
        
        elif "stock prices" in q:
            search = q.split("of")[-1].strip()
            lookup = {'apple':'APPL',
                     'amazon': 'AMZN',
                     'google':'GOOGL'}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speaking(f"found it. The price for {search} is {currentprice}")
                continue
            except:
                speaking("Sorry, I have no data for {search}")
                continue
