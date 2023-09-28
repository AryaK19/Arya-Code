import random as rn

name = input("Enter Your Name :")

c = int(input("Enter The Range You Wanna Play With 1 to:"))

a = rn.randint(1,c)

b = int(input("Enter Your Guess :"))

for i in range(1,c+2):
    if b<a :
        print("You Guessed it Wrong!")
        print("Bigger No. Please")
        b = int(input("Enter Your Guess Again :"))
        no=i+1
        continue
    if b>a :
        print("You Guessed it Wrong!")
        print("Smaller No. Please")
        b = int(input("Enter Your Guess Again :"))
        no=i+1
        continue
    else :
        no=i
        print(f"You got the correct no.Which Was {a} ")
        break

print(f"The No. Of Tries You Took is {no}")

with open("high score.txt") as f:
    p = f.read()
    s = p.split()


if no<int(s[2]) and c ==100:
    p=p.replace(s[0],name)
    p=p.replace(s[2],str(no))

    with open("high score.txt","w") as f :
            f.write(p)

    print("You Have The Highest Score In The Game Till now !!!!!!  ")

else:
    print(f"The High Score Is Of {s[0]}")