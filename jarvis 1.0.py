import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia  
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import pyscreeze
import wolframalpha
import time

engine = pyttsx3.init()
wolframalpha_app_id = '25EYJT-GV5XL7W5G5'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%I:%M%S")
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

   

def wishme():
   speak("Welcome back Meelaad!")
   


   #greeting

   hour = datetime.datetime.now().hour
   if hour>=6 and hour<12:
       speak("Good morning sir!")
   elif hour>=12 and hour<18:
     speak("Good Afternoon sir!")
   elif hour>=18 and hour<24:
        speak("Good Evening sir!")
   else:
        speak("Good Night sir!")
        
   speak("Jarvis at your service. Please tell me how can i help you today?")    

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
     print("Recognizer....")   
     query = r.recognize_google(audio,language='en-US')
     print(query)

    except Exception as e:
       print(e)
       print("say that again please....")  
       return "None"
    return query


def sendEmail(to,conyent):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('melad1999@gmail.com','pass')
    server.sendmail('melad1999@gmail.com',to,)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Ms/Desktop/screenshot.png')
    

def cpu():
    usage= str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    
    battery= psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def joke():
     speak(pyjokes.get_joke())






if __name__ == "__main__":

    wishme()

    while True:
       query = TakeCommand().lower()


       if 'time' in query:
           time_()

       elif 'date' in query:
           date_()

       elif 'wikipedia' in query:
           speak("searching.....")
           query=query.replace('wikipedia','')
           result=wikipedia.summary(query,sentences=3)
           speak('According to wikipedia')
           print(result)
           speak(result)
 
       elif 'send email' in  query:
            try:
                speak("what should i say?")
                content=TakeCommand()
                reciever='reciever_is_me@gmail.com'

                speak("who is the reciver")
                reciever=input("Enter Reciver Email : ")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent')


            except Exception as e:
                print(e)
                speak("Unable to send Email.")


       elif 'search in chrome' in query:
           speak('what should I search?') 
           chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'    

           search = TakeCommand().lower()
           wb.get(chromepath).open_new_tab(search+'.com')

       elif 'search youtube' in query:
           speak('what should i search')  
           search_term = TakeCommand().lower()
           speak("Here we go toy youtube!")   
           wb.open('https://www.youtube.com/results?search_query='+search_term) 

       elif 'search google' in query:
           speak('what should i search')  
           search_term = TakeCommand().lower()
           speak("searching....")   
           wb.open('https://www.google.com/search?q='+search_term)        

 
       elif 'cpu' in query:
           cpu() 
        
       elif 'joke' in query:
           joke()

       elif 'go offline' in query:
           speak('going offline sir!')
           quit()

       elif 'microsoft' in query:
           speak('opening ms word.....') 
           ms_word = r'C:/Program Files/Microsoft Office/Office15/WINWORD.EXE' 
           os.startfile(ms_word)  

       elif 'screenshot' in query:
           screenshot() 

       elif 'remember that' in query:
            speak("what should i remember?")
            memory = TakeCommand()
            speak("youshould asked me to remember that"+ memory)
            remember = open ('memory.txt','w')
            remember.write(memory)
            remember.close()

       elif 'do you remember anything' in query:
           remember= open('memory.txt','r')
           speak ('you asked me to remember that'+remember.read()) 

       elif 'where is' in query:
           query = query.replace("where is","")
           location = query
           speak("User askd to locate" + location)
           wb.open_new_tab("https://www.google.com/maps/place/"+location)

       elif 'calculate' in query:
           client = wolframalpha.Client(wolframalpha_app_id)
           indx = query.lower().split().index('calculate') 
           query = query.split()[indx + 1:]
           res = client.query(''.join(query))
           answer = next(res.results).text
           print('the answer is : '+answer)
           speak('the answer is : '+answer) 
        
       elif 'what is' in query or 'who is' in query:
           client = wolframalpha.Client(wolframalpha_app_id)
           res = client.query(query)

           try:
               print(next(res.results).text)
               speak(next(res.results).text)
           except StopIteration:
               print("no results")

       elif 'stop listening' in query:
           speak('for how many second you want me to stop listening to your commands')
           ans = int(TakeCommand())
           time.sleep(ans)
           print(ans)        
       elif 'log out' in query:
           os.system("shutdown -1")
       elif 'restart' in query:
           os.system("shutdown /r /t 1")    
       elif 'shutdown' in query:
           os.system("shutdown /s /t 1")   






