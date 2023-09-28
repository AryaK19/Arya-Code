from tkinter import*

root = Tk()
root.geometry("444x233")
root.title("PyPiano")

# Important Lable Options

# text - adds Text
# bd  - Background
# fg - Foreground
# font - Sets the font
# padx  - x padding
# pady  - y padding
# relief- border styling,SUNKEN,RAISED,GROOVE ,RIDGE - (For Border Styling)

# can search on google for more

title_lable = Label(text="fcqbgwfygefyfgbccfbbgfcbgfcbgfyygbcgbirbrbcyrgbcbgirbcbbbfbfrfbyygbygbcwbyrfeyrterutreutryte\nybrtebrwerbuyrtbfryturrtbcertbcerutbwuertbwciuerbwciuetbwceiurytbweiruytebrwey",bg= "red",fg="white",padx=23,pady=45,font=("comicsansms",10,"bold"),borderwidth=3,relief=SUNKEN)

# title_lable.pack()

# Important Pack options 

# anchor = nw,ne(north-west,north-east) for side = TOP (se for BOTTOM) 
# side = top,bottom,left,right
# fill - makes it pull as size is increased
# padx
# pady

# title_lable.pack(side=BOTTOM,anchor='sw',fill=X)
# title_lable.pack(side=LEFT,fill=Y)
title_lable.pack(side=LEFT,fill=Y,padx=34,pady=44)





root.mainloop()