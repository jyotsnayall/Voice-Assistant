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
