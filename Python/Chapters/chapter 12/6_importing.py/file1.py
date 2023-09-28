
def greet(name):
    return print(f"Good Morning, {name}.")

#if the def is not run in the main file ( which is this)it will not include this section 

#here __name__ is the name of the file the code id running on 
# print(__name__) will print name of the file . 

if __name__=="__main__":
    #so if name is no main in in the other file it will not run !!!!
    n = input("Enter a name : ")
    greet(n)



