from tkinter import*

root = Tk()
root.geometry("643x333")

def hello():
    print("Hello Tkinker Buttons")
def helloArya():
    print("Hello Arya")

frame = Frame(root,borderwidth=6,bg='grey',relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1 = Button(frame,text="Print Now",command=hello) # have to write only the name of function that you want it to do when the buttons are pressed.....


b1.pack(side=LEFT,padx=2)
b2 = Button(frame,text="Print Now",command=helloArya)
b2.pack(side=LEFT,padx=2)
b3 = Button(frame,text="Print Now")
b3.pack(side=LEFT,padx=2)

root.mainloop()