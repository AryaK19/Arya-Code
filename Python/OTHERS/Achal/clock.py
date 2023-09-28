from tkinter import *
import datetime
import winsound
import speech_recognition as sr


def set_time():
    global hr_set
    global min_set
    global sec_set

    hr_set,min_set,sec_set = takeCommand() 
    date_time()

    
def takeCommand():
    # it takes microphone input from the user and returns str output 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 550
        r.pause_threshold = 1 # wiats if i stop for a while (that is not  to complete the speech)
        r.adjust_for_ambient_noise(source, duration=1)

        print("HOUR : ")
        print("Listening...")
        audio = r.listen(source)

        print("Recognizing...")
        hr_set = r.recognize_google(audio,language="en-IN")
        print(f"User said:{hr_set}\n")
            
        


        print("MINUTE : ")
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
        min_set = r.recognize_google(audio,language="en-IN")
        print(f"User said:{min_set}\n")
         

        print("SECOND : ")
        print("Listening...")
        audio = r.listen(source)
    
        print("Recognizing...")
        sec_set = r.recognize_google(audio,language="en-IN")
        print(f"User said:{sec_set}\n")
       

        return hr_set,min_set,sec_set


def play_alarm():
    winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
    
    
    lab_txt.after(4000,play_alarm)

def date_time():
    time_now = datetime.datetime.now()
    hr = time_now.strftime('%H')
    min = time_now.strftime('%M')
    sec = time_now.strftime('%S')
    
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_txt.config(text=f"{hr_set}:{min_set}:{sec_set}")
    # print(hr_set)
    if int(hr) == int(hr_set) and int(min) == int(min_set) and int(sec) == int(sec_set):
        lab_txt.config(text="Time's Up !!!!!")
        play_alarm()
        
        

    lab_txt.after(200,date_time)
    



clock = Tk()
clock.title('ALARM CLOCK')
clock.geometry("800x500")
clock.config(bg='black')

hr_set,min_set,sec_set = 16,0,0

lab_hr = Label(clock,text="00",font=('italic',60,"bold"),bg='orange',fg='white')
lab_hr.place(x=70,y=100,height=150,width=150)

lab_hr_txt=Label(clock,text="HOUR",font=('italic',30,"bold"),bg='orange',fg='white')
lab_hr_txt.place(x=70,y=300,height=50,width=150)

lab_min=Label(clock,text="00",font=('italic',60,"bold"),bg='orange',fg='white')
lab_min.place(x=326,y=100,height=150,width=150)

lab_min_txt=Label(clock,text="MIN",font=('italic',30,"bold"),bg='orange',fg='white')
lab_min_txt.place(x=326,y=300,height=50,width=150)

lab_sec=Label(clock,text="00",font=('italic',60,"bold"),bg='orange',fg='white')
lab_sec.place(x=582,y=100,height=150,width=150)

lab_sec_txt=Label(clock,text="SEC",font=('italic',30,"bold"),bg='orange',fg='white')
lab_sec_txt.place(x=582,y=300,height=50,width=150)

lab_txt=Label(clock,text="00",font=('italic',20,"bold"),bg='orange',fg='white')
lab_txt.place(x=255,y=450,height=40,width=300)

button = Button(clock,text = "Set Alarm",font=('italic',0,"bold"),bg='white',fg="orange",width = 20,command = set_time).place(x =270,y=400)

date_time()

clock.mainloop()