from tkinter import*


root = Tk()

root.geometry("655x333")

f1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN,)
f1.pack(side=LEFT,fill=Y,pady=40)

f2 = Frame(root,bg="grey",borderwidth=9,relief=SUNKEN)
f2.pack(side=TOP,fill=X)


l = Label(f1,text="Projet tkinter - Pycharm")
l.pack(pady=42)
l = Label(f2,text="Projet tkinter - Pycharm",font=("Helvetica",16,"bold"),fg='red',pady=34)
l.pack()



root.mainloop()