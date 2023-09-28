# to print tables from 2 to 20

for a in range(2,21):
    for i in range(1,11): 
            b=str(a)+' x '+str(i)+' = '+str(a*i)
            with open("D:\python arya\chapter 9\problem set\\3.py\Tables 2-20.txt",'a') as f:
                f.write(str(b)+'\n')
            if i == 10 :
                with open("D:\python arya\chapter 9\problem set\\3.py\Tables 2-20.txt",'a') as f:
                    f.write('\n')

    
