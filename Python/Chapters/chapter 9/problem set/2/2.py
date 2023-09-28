def game():
    return 8

score = int(game())

with open('D:\python arya\chapter 9\problem set\\2\Hi_score.txt') as f :
    a = (f.read())
   
if a =='':
    with open("D:\python arya\chapter 9\problem set\\2\Hi_score.txt",'w') as f:
        f.write(str(score))
    print("You beat the high score") 

elif int(a) >= score :
    print("You didn't beat the high score")
else :
    with open("D:\python arya\chapter 9\problem set\\2\Hi_score.txt",'w') as f:
        f.write(str(score))
    print("You beat the highest score")
