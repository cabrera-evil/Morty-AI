'''
    Description:
    Create your own virtual assistant with python.
    Author: Douglas Cabrera AKA EvilMorty
    Version: 2.0
'''

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import json
import spoty
import webbrowser
from playsound import playsound

engine = pyttsx3.init()
# name of the virtual assistant
name = 'morty'
attemts = 0

# get voices and select on of them
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# keys
with open('src/keys.json') as json_file:
    keys = json.load(json_file)

# colors
green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"
normal_color = "\033[0;37;40m"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# listener v2
def get_audio():
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f"{green_color} Listening...{normal_color}")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec or 'muerte' in rec or 'marty' in rec:
                rec = rec.replace(f"{name} ", "").replace("muerte", "").replace("marty", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
            else:
                print(f"Vuelve a intentarlo, no reconozco: {rec}")
        except:
            pass
    return {'text':rec, 'status':status}

import voice
# voice commands v2
while True:
    rec_json = get_audio()

    rec = rec_json['text']
    status = rec_json['status']

    if status:
        if 'estas ahi' in rec:
            print('Si, estoy aqui')

        elif 'reproduce' in rec:
            if 'spotify' in rec:
                music = rec.replace('reproduce spotify', '')
                print(f'Reproduciendo{music}')
                playsound(voice.Voy_a_Intentarlo) 
                spoty.play(keys["spoty_client_id"], keys["spoty_client_secret"], music)
            else:
                music = rec.replace('reproduce', '')
                print(f'Reproduciendo{music}')
                pywhatkit.playonyt(music)
                playsound(voice.Voy_a_Intentarlo) 

        elif 'git' in rec or 'repo' in rec:
            print("Abriendo repositorio de github")
            webbrowser.open("https://github.com/cabrera-evil/Morty-AI", new=0, autoraise=True)
            playsound(voice.Ambos_son_Geniales)

        elif 'que' in rec:
            if 'hora' in rec:
                time = datetime().now.strftime('%H:%M %p')
                talk(f"Son las {time}")

        elif 'busca' in rec:
            order = rec.replace('busca', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(order, 1)
            talk(info)
            
        elif 'domina' in rec:
            print('Ahora Morty domina el mundo')
            playsound(voice.Voy_a_Intentarlo) 

        elif 'eres' in rec:
            print("Morty se siente halagado")
            playsound(voice.Halagador)

        elif 'descansa' in rec:
            print("Thanks for use Morty Assistant")
            playsound(voice.Gracias)
            break

        else:
            print(f"Vuelve a intentarlo, no reconozco: {rec}")
        
        attemts = 0
    else:
        attemts += 1