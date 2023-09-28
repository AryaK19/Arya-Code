from tkinter import *
import os
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
from stegano import lsb
from tkinter.filedialog import asksaveasfilename


pbl=Tk()
pbl.title("IMAGE STEGANOGRAPHY")
pbl.geometry("1400x800")
pbl.config(bg="light blue")

file = open("password.txt","r")
password = file.read()

def showimage():
    global r
    r=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image",filetype=(("PNG file",'.png'),("JPG file",".jpg"),("All file","*.txt")))
    pbl4=Image.open(r)
    pbl4=ImageTk.PhotoImage(pbl4)
    LBL.configure(image=pbl4,width=350,height=350)
    LBL.image=pbl4

def Hide():
    global secret
    Message=text1.get(1.0,END)

    secret=lsb.hide(str(r),Message)


def Show():
    
    if password == inp.get():
        lable.config(bg="white")
        clear_message=lsb.reveal(r)
        text1.delete(1.0,END)
        text1.insert(END,clear_message)
    else:
        lable.config(bg="red")

def save():
    secret.save("hidden.png")

inp = StringVar()

#IMAGE FRAME
lable=Label(pbl,text= "Enter Password",font="helvetica",bg="white",fg="blue",relief=GROOVE)
lable.place(x=590,y=270)
Entry= Entry(pbl,textvariable = inp,bg = "pink",width = 15).place(x=600,y=300)

frame1=Frame(pbl,background="black",bd=6,width=500,height=500,relief=SUNKEN)
frame1.place(x=55,y=60)
LBL=Label(frame1,bg="yellow")
LBL.place(x=80,y=10)
#text frame
frame2=Frame(pbl,background="white",bd=6,width=500,height=500,relief=SUNKEN)
frame2.place(x=750,y=60)
text1=Text(frame2,font="helvetica",bg="white",fg="blue",relief=GROOVE)
text1.place(x=0,y=0,width=500,height=500)
#open image and save image button box
#frame3
frame3=Frame(pbl,bd=3,bg="yellow",width=500,height=150,relief=SOLID)
frame3.place(x=50,y=600)
buttonbox1=Button(frame3,text="View Image",width=15,height=4,font="algerian",command=showimage).place(x=20,y=30)
buttonbox1=Button(frame3,text="Save Image",width=15,height=4,font="algerian",command=save).place(x=240,y=30)
photo=Label(pbl,text="Photo(.jpg,.png,.jpeg)",font="algerian",fg="red").place(x=60,y=605)
#frame4
#hide data and save data button box
frame4=Frame(pbl,bd=3,bg="yellow",width=500,height=150,relief=SOLID)
frame4.place(x=750,y=600)
buttonbox2=Button(frame4,text="hide data",width=15,height=4,font="algerian",command=Hide).place(x=20,y=30)
buttonbox2=Button(frame4,text="show data",width=15,height=4,font="algerian",command=Show).place(x=240,y=30)
photo=Label(pbl,text="Photo(.jpg,.png,.jpeg)",font="algerian",fg="red").place(x=60,y=605)




pbl.mainloop()