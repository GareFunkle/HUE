import random
import subprocess
import json
import os
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time


listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate +15)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 0.5)
voices = engine.getProperty('voices')[38]
engine.setProperty('voice', voices.id)
heure = datetime.datetime.now().strftime('%H:%M')
wikipedia.set_lang("fr")





def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Bonjour Monsieur, il est' + heure + 'avez-vous bien dormi ?')
        
    elif hour >= 12 and hour < 18:
        talk('Bonjour Monsieur, il est' + heure + 'avez-vous passer une bonne matinée?')
        
    else:
        talk('Bonsoir Monsieur, il est' + heure + 'avez-vous passer une bonne journée?')
        


def take_command():
    try:
        command = ''
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='fr-FR')
            command = command.lower()
            if "you" in command:
                command = command.replace('you', '')
                print(command)
    except:
        pass
    return command

def run_you():
    command = take_command()
    print(command)
    
    if 'trouve-moi' in command:
        search = command.replace('trouve-moi', '')
        pywhatkit.search(search)
        talk('jai trouver ca sur google')
    elif 'met moi de la musique' in command:
        song = command.replace('met moi de la musique', '')
        pywhatkit.playonyt(song)
        talk('jai trouver ca sur youtube')
    elif 'quelle heure est-il' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        talk('Il est' + heure)
    elif 'temps' in command:
        api_key = "Api key"
        base_url = "https://api.openweathermap.org/data/3.0/weather?"
        talk('Nom de la ville')
        print("Nom de ville : ")
        city_name = take_command()
        complete_url = base_url + "appid = " + api_key + "&q = " + city_name
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print("Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidity) + "\n description = " + str(weather_description))
        else:
            talk('je nai pas trouver la ville')
    elif 'you ca va ?' in command:
        talk('oui tout vas bien')
    elif 'qui est' in command:
        person = command.replace('qui est ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'oui et toi' in command:
        talk('Oui jai passer une bonne journée merci!')
    elif 'blague' in command:
        talk(pyjokes.get_joke(language="fr", category="neutral"))
    elif 'plus besoin de toi' in command:
        talk('pendant combien de temps je vous laisse tranquille?')
        a = int(take_command())
        talk('Daccord a tout à lheure')
        time.sleep(a)
        print(a)
    elif 'tu vas bien' in command:
        talk('Oui ca va ')        
    elif 'tu es là' in command:
        talk('Oui Vincent je suis bien la !')
    elif 'qui es-tu' in command:
        talk("Je vien d'une simple idee de la part de mon createur Vincent")
    else:
        talk('Je nai pas entendu ')
        

wishMe()
while True:
    run_you()