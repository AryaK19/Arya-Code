from tkinter import*
# This is to add JPJ file in python
from PIL import Image,ImageTk

root = Tk()

# To set height and width
root.geometry("455x244")

# for png files
photo = PhotoImage(file="donut final.png")
photoLable = Label(image=photo)
photoLable.pack()

# For jpj file

# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)

root.mainloop()