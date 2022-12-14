

import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import subprocess
import os
import cv2
import random
from requests import get
import smtplib
import psutil
import instaloader
import pyautogui
import PyPDF2
from PIL import ImageGrab
import pyaudio
import wave
import numpy as np 
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ALOYUi import Ui_ALOYUI
from state import state
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import qrcode




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Intro()
    
    
    def take_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command1 = listener.recognize_google(voice,language='en-in')
                command1 = command1.lower()  
                if 'ALOY' in command1: 
                    command1 = command1.replace('ALOY','')
                
            return command1
        except:
            return 'None'
        
    
    def run_ALOY(self):
        self.talk('Greetings , This is Aloy ... here at your service')
        self.wish()
        while True:
            self.command = self.take_Command() 
            print(self.command)
            if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) : 
                
                self.yt(self.command) 
            
            elif ('your age' in self.command) or ('are you single'in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('i love you' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
                self.Fun(self.command)
            elif 'time' in self.command : 
                self.Clock_time(self.command)
            elif (('hi' in self.command) and len(self.command)==2) or ((('hai' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
                self.comum(self.command)
            elif ('what can you do' in self.command) or ('your name' in self.command) or ('palash das wikipedia' in self.command) or ('university name' in self.command):
                self.Fun(self.command)
            elif ('joke'in self.command) or ('date' in self.command):
                self.Fun(self.command)
            
            elif ("college time table" in self.command) or ("schedule" in self.command):
                self.shedule() 
            
            elif ("today" in self.command):
                day = self.Cal_day()
                self.talk("Today is "+day)
            
            
            
            elif ("meeting" in self.command):
                self.talk("Ok sir opening meeet")
                webbrowser.open("https://meeting/")
            
            
            
    
            
            
            elif ('facebook' in self.command) or ('whatsapp' in self.command) or ('instagram' in self.command) or ('twitter' in self.command) or ('discord' in self.command) or ('social media' in self.command):
                self.social(self.command)
            
            
            elif ('hotstar' in self.command) or ('prime' in self.command) or ('netflix' in self.command):
                self.OTT(self.command)
            
            elif ('online classes'in self.command):
                self.OnlineClasses(self.command)
            
            elif ('open teams'in self.command) or ('open stream'in self.command) or ('open sharepoint'in self.command) or('open outlook'in self.command)or('open amrita portal'in self.command)or('open octave'in self.command):
                self.college(self.command)
            
            
            elif ('wikipedia' in self.command) or ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command):
                self.B_S(self.command)
            
            elif ('open google'in self.command) or ('open edge'in self.command) :
                self.brows(self.command)
            
            elif ('open gmail'in self.command) or('open maps'in self.command) or('open calender'in self.command) or('open documents'in self.command )or('open spredsheet'in self.command) or('open images'in self.command) or('open drive'in self.command) or('open news' in self.command):
                self.Google_Apps(self.command)
            
            
            elif ('open github'in self.command) or ('open gitlab'in self.command) :
                self.open_source(self.command)
            
            elif ('slides'in self.command) or ('canva'in self.command) :
                self.edit(self.command)
            
            
            elif ('open calculator'in self.command) or ('open notepad'in self.command) or ('open paint'in self.command) or ('open online classes'in self.command) or ('open discord'in self.command) or ('open ltspice'in self.command) or ('open editor'in self.command) or ('open spotify'in self.command) or ('open steam'in self.command) or ('open media player'in self.command):
                self.OpenApp(self.command)
            
            
            elif ('close calculator'in self.command) or ('close notepad'in self.command) or ('close paint'in self.command) or ('close discord'in self.command) or ('close ltspice'in self.command) or ('close editor'in self.command) or ('close spotify'in self.command) or ('close steam'in self.command) or ('close media player'in self.command):
                self.CloseApp(self.command)
            
            
            elif ('flipkart'in self.command) or ('amazon'in self.command) :
                self.shopping(self.command)
            
            elif ('where i am' in self.command) or ('where we are' in self.command):
                self.locaiton()
            
            
            elif ('command prompt'in self.command) :
                self.talk('Opening command prompt')
                os.system('start cmd')
            
            
            elif ('instagram profile' in self.command) or("profile on instagram" in self.command):
                self.Instagram_Pro()
            
            
            elif ('take screenshot' in self.command)or ('screenshot' in self.command) or("take a screenshot" in self.command):
                self.scshot()
            
            
            
            
            
            elif "activate mod" in self.command:
                self.How()
            
            
            elif ("volume up" in self.command) or ("increase volume" in self.command):
                pyautogui.press("volumeup")
                self.talk('volume increased')
            
            
            elif ("volume down" in self.command) or ("decrease volume" in self.command):
                pyautogui.press("volumedown")
                self.talk('volume decreased')
            
            
            elif ("volume mute" in self.command) or ("mute the sound" in self.command) :
                pyautogui.press("volumemute")
                self.talk('volume muted')
            
            
            elif ("open mobile cam" in self.command):
                self.Mobilecamra()
            
            
            elif ('web cam'in self.command) :
                self.webCam()
            
            elif("create a new contact" in self.command):
                self.AddContact()
            
            elif("number in contacts" in self.command):
                self.NameIntheContDataBase(self.command)
            
            elif("display all the contacts" in self.command):
                self.Display()
            
            
            elif ("covid" in self.command) or  ("corona" in self.command):
                self.talk(" which state covid 19 status do you want to check")
                s = self.take_Command()
                self.Covid(s)
            
            
            elif ("recording" in self.command) or ("screen recording" in self.command) or ("voice recording" in self.command):
                try:
                    self.talk(" press q key to stop recordings")
                    option = self.command
                    Record_Option(option=option)
                    self.talk(" recording is being saved")
                except:
                    self.talk(" an unexpected error occured couldn't start screen recording")
            
            elif ("track" in self.command) or ("track a mobile number" in self.command):
                self.talk(" please enter the mobile number with country code")
                try:
                    location,servise_prover,lat,lng=Phonenumber_location_tracker()
                    self.talk(f" the mobile number is from {location} and the service provider for the mobile number is {servise_prover}")
                    self.talk(f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}")
                    print(location,servise_prover)
                    print(f"Latitude : {lat} and Longitude : {lng}")
                    self.talk(" location of the mobile number is saved in Maps")
                except:
                    self.talk(" an unexpected error occured couldn't track the mobile number")
            
            
            elif 'music' in self.command:
                try:
                    music_dir = 'E:\\music' 
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))
                except:
                    self.talk(" an unexpected error occured")
            
            
            elif 'ip address' in self.command:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                self.talk(f"your IP address is {ip}")
            
            
            
            elif ('send a message' in self.command):
                self.whatsapp(self.command)
            
            
            elif 'send email' in self.command:
                self.verifyMail()
            
            
            elif "temperature" in self.command:
                self.temperature()
            
            elif "create a qr code" in self.command:
                self.qrCodeGenerator()
            
            
            elif "internet speed" in self.command:
                self.InternetSpeed()
            
            
            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay , I am going to sleep you can call me anytime.")
                break
            
            
            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk(", I am not sleeping, I am in online, what can I do for u")
            
            
            elif ("goodbye" in self.command) or ("get lost" in self.command):
                self.talk("Have a great day . Peace Out")
                sys.exit()
            
            
            elif ('system condition' in self.command) or ('condition of the system' in self.command):
                self.talk("checking the system condition")
                self.condition()
            
            
            elif ('tell me news' in self.command) or ("the news" in self.command) or ("todays news" in self.command):
                self.talk("Please wait , featching the latest news")
                self.news()
            
            
            elif ('shutdown the system' in self.command) or ('down the system' in self.command):
                self.talk(" shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")
            
            
            elif 'restart the system' in self.command:
                self.talk(" restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")
            
            
            elif 'sleep the system' in self.command:
                self.talk(" the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
            
                
    
    def talk(self,text):
        engine.say(text)
        engine.runAndWait()

    
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        self.talk(f"today is {day} and its {t}")
       

    
    def temperature(self):
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        self.talk(f"current {search} is {temp}")
    
    

    
    def Mobilecamra(self):
        import urllib.request
        import numpy as np
        try:
            self.talk(f" openinging mobile camera")
            URL = "http://_IP_Webcam_IP_address_/shot.jpg" 
            while True:
                imag_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(imag_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    self.talk(f" closing mobile camera")
                    break
            cv2.destroyAllWindows()
        except Exception as e:
            print("Some error occured")

    
    
    def webCam(self):    
        self.talk('Opening camera')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('web camera',img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    
   
    def whatsapp(self,command):
        try:
            command = command.replace('send a message to','')
            command = command.strip()
            name,numberID,F = self.SearchCont(command)
            if F:
                print(numberID)
                self.talk(f', what message do you want to send to {name}')
                message = self.take_Command()
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                print(hour,min)
                if "group" in command:
                    kit.sendwhatmsg_to_group(numberID,message,int(hour),int(min)+1)
                else:
                    kit.sendwhatmsg(numberID,message,int(hour),int(min)+1)
                self.talk(" message have been sent")
            if F==False:
                self.talk(f', the name not found in our data base, shall I add the contact')
                AddOrNot = self.take_Command()
                print(AddOrNot)
                if ("yes" in AddOrNot) or ("add" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                    self.AddContact()
                elif("no" in AddOrNot):
                    self.talk('Ok ')
        except:
            print("Error occured, please try again")

    


    
    def InternetSpeed(self):
        self.talk("Wait a few seconds , checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) 
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        self.talk(f", we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
        
    

    
    def comum(self,command):
        print(command)
        if ('hi'in command) or('hai'in command) or ('hey'in command) or ('hello' in command) :
            self.talk("Hello , how may I be of service ?")
        else :
            self.No_result_found()

    
    def Fun(self,command):
        print(command)
        if 'your name' in command:
            self.talk("My name is Aloy")
        elif 'university name' in command:
            self.talk("You are studing Computer Science and Engineering in Indian Institute of Technology Jodhpur") 
        elif 'what can you do' in command:
            self.talk("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in command:
            self.talk("I am younger than you")
        elif 'date' in command:
            self.talk('Sorry not intreseted, I am having headache, we will catch up some other time')
        elif 'are you single' in command:
            self.talk('No, I am in a relationship with Siri')
        elif 'joke' in command:
            self.talk(pyjokes.get_joke())
        elif 'are you there' in command:
            self.talk('Yes  I am here')
        elif 'tell me something' in command:
            self.talk(',You tell me something and I will help you with it')
        elif 'thank you' in command:
            self.talk(', I am here to help you')
        elif 'in your free time' in self.command:
            self.talk(', in my free time , I enjoy the company of Alexa')
        elif 'i love you' in command:
            self.talk('I love you too ')
        elif 'can you hear me' in command:
            self.talk('Yes , I can hear you')
        elif 'do you ever get tired' in command:
            self.talk('It would be impossible to tired of our conversation')
        else :
            self.No_result_found()

    
    def social(self,command):
        print(command)
        if 'facebook' in command:
            self.talk('opening your facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'whatsapp' in command:
            self.talk('opening your whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'instagram' in command:
            self.talk('opening your instagram')
            webbrowser.open('https://www.instagram.com/')
        elif 'twitter' in command:
            self.talk('opening your twitter')
            webbrowser.open('https://twitter.com/Suj8_116')
        elif 'discord' in command:
            self.talk('opening your discord')
            webbrowser.open('https://discord.com/channels/@me')
        else :
            self.No_result_found()
        
    
    def Clock_time(self,command):
        print(command)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        self.talk("Current time is "+time)
    
    
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week

    
    
    def shedule(self):
        day = self.Cal_day().lower()
        self.talk(" Schedule of ")
        Week = {"monday" : "from 10:00 am you have Operating system class . from 11:00 am  you have Principle of Programming Language class. From 2:30 pm you have Design and Analysis of Algorithm class . from 4:00 pm you have database management systems class . from 5pm you have Professional Ethics class after that you are free . Enjoy your day"
        }
        if day in Week.keys():
            self.talk(Week[day])

    
    
    def college(self,command):
        print(command)
        if 'teams' in command:
            self.talk('opening your microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')
        elif 'meet' in command:
            self.talk('opening your google meet')
            webbrowser.open('https://meet.google.com/')
        elif 'stream' in command:
            self.talk('opening your microsoft stream')
            webbrowser.open('https://web.microsoftstream.com/')
        elif 'outlook' in command:
            self.talk('opening your microsoft school outlook')
            webbrowser.open('https://outlook.office.com/mail/')
        elif 'octave' in command:
            self.talk('opening Octave online')
            webbrowser.open('https://octave-online.net/')
        else :
            self.No_result_found()
    
    


    
    def B_S(self,command):
        print(command)
        try:
            
            if ('wikipedia' in command):
                target1 = command.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is meant by' in command):
                target1 = command.replace("what is meant by"," ")
            elif('tell me about' in command):
                target1 = command.replace("tell me about"," ")
            elif('who is' in command):
                target1 = command.replace("who is"," ")
            print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            self.talk("according to wikipedia "+info)
        except :
            self.No_result_found()
        
    
    def brows(self,command):
        print(command)
        if 'google' in command:
            self.talk(",What do you want to search..")
            S = self.take_Command()
            webbrowser.open(f"{S}")
        elif 'edge' in command:
            self.talk('opening Miscrosoft edge')
            os.startfile('..\\..\\MicrosoftEdge.exe')
        else :
            self.No_result_found()

    
    
    def Google_Apps(self,command):
        print(command)
        if 'gmail' in command:
            self.talk('opening your google gmail')
            webbrowser.open('https://mail.google.com/mail/')
        elif 'maps' in command:
            self.talk('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/')
        elif 'news' in command:
            self.talk('opening google news')
            webbrowser.open('https://news.google.com/')
        elif 'calender' in command:
            self.talk('opening google calender')
            webbrowser.open('https://calendar.google.com/calendar/')
        elif 'photos' in command:
            self.talk('opening your google photos')
            webbrowser.open('https://photos.google.com/')
        elif 'documents' in command:
            self.talk('opening your google documents')
            webbrowser.open('https://docs.google.com/document/')
        elif 'spreadsheet' in command:
            self.talk('opening your google spreadsheet')
            webbrowser.open('https://docs.google.com/spreadsheets/')
        else :
            self.No_result_found()
            
    
    def yt(self,command):
        print(command)
        if 'play' in command:
            self.talk(" can you please say the name of the song")
            song = self.take_Command()
            if "play" in song:
                song = song.replace("play","")
            self.talk('playing '+song)
            print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in command:
            self.talk(" please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            self.talk(f" downloaded {yt.title} from the link you given into the main folder")
        elif 'youtube' in command:
            self.talk('opening youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()
        


    
    def edit(self,command):
        print(command)
        if 'slides' in command:
            self.talk('opening google slides')
            webbrowser.open('https://docs.google.com/presentation/')
        elif 'canva' in command:
            self.talk('opening canva')
            webbrowser.open('https://www.canva.com/')
        else :
            self.No_result_found()

    
    def OTT(self,command):
        print(command)
        if 'hotstar' in command:
            self.talk('opening  disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif 'prime' in command:
            self.talk('opening  amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif 'netflix' in command:
            self.talk('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        else :
            self.No_result_found()

    
    
    
    
    def OpenApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk('Opening calculator')
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif ('paint'in command) :
            self.talk('Opening msPaint')
            os.startfile('c:\\Windows\\System32\\mspaint.exe')
        elif ('notepad'in command) :
            self.talk('Opening notepad')
            os.startfile('c:\\Windows\\System32\\notepad.exe')
        elif ('discord'in command) :
            self.talk('Opening discord')
            os.startfile('..\\..\\Discord.exe')
        elif ('editor'in command) :
            self.talk('Opening  Visual studio code')
            os.startfile('..\\..\\Code.exe')
        elif ('online classes'in command) :
            self.talk('Opening  Microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')
        elif ('spotify'in command) :
            self.talk('Opening spotify')
            os.startfile('..\\..\\Spotify.exe')
        elif ('lt spice'in command) :
            self.talk('Opening lt spice')
            os.startfile("..\\..\\XVIIx64.exe")
        elif ('steam'in command) :
            self.talk('Opening steam')
            os.startfile("..\\..\\steam.exe")
        elif ('media player'in command) :
            self.talk('Opening VLC media player')
            os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
        else :
            self.No_result_found()
            
    
    def CloseApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk("okay , closeing caliculator")
            os.system("taskkill /f /im calc.exe")
        elif ('paint'in command) :
            self.talk("okay , closeing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('notepad'in command) :
            self.talk("okay , closeing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('discord'in command) :
            self.talk("okay , closeing discord")
            os.system("taskkill /f /im Discord.exe")
        elif ('editor'in command) :
            self.talk("okay , closeing vs code")
            os.system("taskkill /f /im Code.exe")
        elif ('spotify'in command) :
            self.talk("okay , closeing spotify")
            os.system("taskkill /f /im Spotify.exe")
        elif ('lt spice'in command) :
            self.talk("okay , closeing lt spice")
            os.system("taskkill /f /im XVIIx64.exe")
        elif ('steam'in command) :
            self.talk("okay , closeing steam")
            os.system("taskkill /f /im steam.exe")
        elif ('media player'in command) :
            self.talk("okay , closeing media player")
            os.system("taskkill /f /im vlc.exe")
        else :
            self.No_result_found()

    
    def shopping(self,command):
        print(command)
        if 'flipkart' in command:
            self.talk('Opening flipkart online shopping website')
            webbrowser.open("https://www.flipkart.com/")
        elif 'amazon' in command:
            self.talk('Opening amazon online shopping website')
            webbrowser.open("https://www.amazon.in/")
        else :
            self.No_result_found()

    
    def verifyMail(self):
        try:
            self.talk("what should I say?")
            content = self.take_Command()
            self.talk("To whom do u want to send the email?")
            to = self.take_Command()
            self.SendEmail(to,content)
            self.talk("Email has been sent to "+str(to))
        except Exception as e:
            print(e)
            self.talk("Sorry sir I am not not able to send this email")
    
    
    def SendEmail(self,to,content):
        print(content)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("YOUR_MAIL_ID","PASWORD")
        server.sendmail("YOUR_MAIL_ID",to,content)
        server.close()

    
    def locaiton(self):
        self.talk("Wait , let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            self.talk(f" i am not sure, but i think we are in {city} city of {state} state of {country} country")
            self.talk(f"and , we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            self.talk("Sorry , due to network issue i am not able to find where we are.")
            pass

    
    def Instagram_Pro(self):
        self.talk(" please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        self.talk(" would you like to download the profile picture of this account.")
        cond = self.take_Command()
        if('download' in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            self.talk("I am done , profile picture is saved in your main folder. ")
        else:
            pass

    
    def scshot(self):
        self.talk(", What should I name the screenshot file")
        name = self.take_Command()
        self.talk("Please  hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.talk("The screenshot is saved in main folder.")

    
    def news(self):
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=YOUR_NEWS_API_KEY"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] 
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            self.talk(f"todays {seq[i]} news is: {headings[i]}")
        self.talk(" I am done, I have read most of the latest news")

    
    def condition(self):
        usage = str(psutil.cpu_percent())
        self.talk("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        self.talk(f" our system have {percentage} percentage Battery")
        if percentage >=75:
            self.talk(f" we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            self.talk(f" we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            self.talk(f" we don't have enough power to work, please connect to charging")
        else:
            self.talk(f" we have very low power, please connect to charging otherwise the system will shutdown very soon")
        
    
    def No_result_found(self):
        self.talk(' I couldn\'t understand, could you please say it again.')        

startExecution = MainThread()
class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_ALOYUI()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)
    
    
    def startTask(self):
        
      
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.run_ALOY()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

app = QApplication(sys.argv)
ALOY = Main()
ALOY.show()
exit(app.exec_())