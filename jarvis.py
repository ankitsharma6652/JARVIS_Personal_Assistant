import wikipedia
import speech_recognition as sr
import datetime
import pyttsx3
import configparser as c
import config
import smtplib
import webbrowser
import os
from time import sleep
from plyer import notification 


def speak(text):
    engine = pyttsx3.init('sapi5')

    voices=engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
    # print(engine.runAndWait)
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak('Good Morning')

    elif hour>=12 and hour<18:
        
        speak('Good Afternoon')
        
    else:
        speak('Good Evening ')

    speak('I am Jarvis Sir,How may i help u?')
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening') 
        # r.pause_threshold=1
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1) 

        audio=r.listen(source)
    try:
        print('Recognizing')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
    except Exception as e:
        print('Say that again please...')
        return "None"
    return query
def send_mail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(config.username,config.password)
    server.sendmail(config.username,to,content)
    server.close()
if __name__ == "__main__":
    # speak('\tHello How may i help u')
        notification.notify( title = "JARVIS HERE", message=" MR.Ankit's Personal Assistant" ,app_name='JARVIS',app_icon='jarvis.ico', timeout=10) # waiting time 
    # sleep(60*60)
    # from win10toast import  ToastNotifier
    # notif_ = ToastNotifier()
    # notif_.show_toast("JARVIS HERE","Mr.Ankit's Personal Assistant", 
    # duration=20,icon_path="jarvis.ico")
        wishme()
    # while True:
        
        query=takeCommand().lower()
        if 'send mail' in query:
            try:
                print('What Should i say')
                content=takeCommand()
                to='abc@gmail.com'
                send_mail(to,content)
                speak('  Email has been sent!')
            except Exception as e:
                print(e)
                speak('   Sorry Sir.I am unable to send mail')
        elif 'open google chrome' in query:
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome')
            speak('opening google chrome')
        elif 'vs code' in query:
            try:
                os.startfile(r'C:\Users\muani\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code')
            except Exception as e:
                speak('Sorry Sir.I am not able to open vs code')
            else:
                speak('\topening vs code')
        elif 'who are you' or  'what"s your name' in query:
            speak('I am Jarvis,Mr. Ankit"s Personal Assistant')


