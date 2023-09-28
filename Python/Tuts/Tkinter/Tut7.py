from tkinter import*
def getvals():
    print(user_value.get())
    print(password_value.get())
    
root = Tk()
root.geometry("655x333")
user = Label(root,text="Username")
password = Label(root,text="Password")

#this is to pack according to grid
# Have to specify rows for this

user.grid()
password.grid(row=1)

# Variable Classes in tkinter

# boolean var , double var ,int var string var

user_value =  StringVar() 
password_value =  StringVar()

user_entry = Entry(root,textvariable=user_value)
pass_entry = Entry(root,textvariable=password_value)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()