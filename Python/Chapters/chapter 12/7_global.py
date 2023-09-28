a = 54 #Global Variable

def func1():
    global a
    print(a)
    a = 8 #Local  Variable
    print(a)

func1()
print(a)

#which means in def a new value is needed to be asigned 

# ___________________________________________________________________________#
print("---")
# ___________________________________________________________________________#


a = 54 #Global Variable

def func1():
    a = 8 #Local  Variable
    print(a)

func1()
print(a)