from tkinter import*

root = Tk()

# To set height and width
root.geometry("600x300")

# width , height
root.minsize(200,100)

root.maxsize(1370,760)

lable = Label(text="PyPiano")
lable.pack()

root.mainloop()

