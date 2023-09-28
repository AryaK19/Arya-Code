#To enter tables in seperate text files 

for i in range(2,21):
    with open(f"D:\python arya\chapter 9\problem set\\3\\tables\Table of {i}.txt",'w')as f:
        for a in range(1,11):
            f.write(f"{i} x {a} = {i*a}")
            if a != 10:
                f.write("\n")