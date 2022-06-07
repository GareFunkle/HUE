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


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')[38]
engine.setProperty('voice', voices.id)



def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Bonjour Vincent, a tu bien dormi ?')
        
    elif hour >= 12 and hour < 18:
        talk('Bonjour Vincent, a tu passer une bonne matinée?')
        
    else:
        talk('Bonsoir Vincent, as tu passer une bonne journée?')
        



def take_command():
    try:
        command = ''
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='fr-FR')
            command = command.lower()
            if "You" in command:
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
    elif 'joue moi' in command:
        song = command.replace('joue moi', '')
        pywhatkit.playonyt(song)
        talk('joue' + song)
    elif 'quelle heure est-il' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Il est' + time)
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
    elif 'qui est' in command:
        person = command.replace('qui est ', '')
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'oui et toi' in command:
        talk('Oui jai passer une bonne journée merci!')
    elif 'blague' in command:
        talk(pyjokes.get_joke())
    elif 'térence' in command:
        talk('terence est un viking dans lame pret a ce battre pour ce quil veux')
    elif 'édouard' in command: 
        talk('édouard est super je nai jamais vu une personne aussi remarquable' )
    elif 'angie' in command:
        talk('angie est une personne formidable qui vien de finir ces examens et je sais bien que tu laime tres fort vincent')
    else:
        talk('Je nai pas entendu ')
        

wishMe()
while True:
    run_you()