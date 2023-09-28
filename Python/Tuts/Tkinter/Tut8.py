from tkinter import*

root = Tk()

root.geometry("655x333")

def getvals():
    print(nameval.get())
    print(phoneval.get())
    print(genderval.get())
    print(ageval.get())
    print(paymentmodeval.get())
    print(foodserviceval.get())

# Made heading
Label(root,text="Welcome to Arya Travels", font="comicsansms 13 bold",pady=15).grid(row=0,column=5)

# text for form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
age = Label(root, text="Age")
paymentmode = Label(root, text="Payment Mode")

# packed that text according to grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
age.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# Made Tkinter Variable to store Entries
nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
ageval = StringVar()
paymentmodeval = StringVar()
foodserviceval = IntVar()

# Entries for the form
nameentry = Entry(root , textvariable=nameval)
phoneentry = Entry(root , textvariable=phoneval)
genderentry = Entry(root , textvariable=genderval)
ageentry = Entry(root , textvariable=ageval)
paymententry = Entry(root , textvariable=paymentmodeval)


# Packing the entries
nameentry.grid(row=1 , column=5)
phoneentry.grid(row=2 , column=5)
genderentry.grid(row=3 , column=5)
ageentry.grid(row=4 , column=5)
paymententry.grid(row=5 , column=5)

# checkbox adding
foodservice = Checkbutton(text="Want to prebook your meals?",variable=foodserviceval)# used vriable to assing it to the foodserviceval 
foodservice.grid(row=7,column=2)

# button and packing it and assigning it a command
Button(text="Submit to Arya Travels",command=getvals).grid(row=8,column=4)


root.mainloop()