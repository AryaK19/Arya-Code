#curency converter

inr=int(input("Enter The Value Of : "))

with open("3\\rates.txt") as f :
    read = f.read()
    p = read.split("	")
for  i in range(0,(53*3),3):
    print(p[i])

name = input("Enter Any Of The Above Names You Wanna Convert To :\n")
no = p.index(name)
    
print(f"The Value of Rs.{inr} in {name} is {inr/float(p[no+2])}")



