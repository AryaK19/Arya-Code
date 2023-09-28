print("FUNCTIONS")
def greet_user(name):
    print(f"Hey {name}")
greet_user("Narayan")

def greet_USER(name, sname):
    print(f"Hey, {name}. You are {sname}'s kid, right?")

greet_USER(input(), input())

def square(num):
    print(num*num)

print(square(4))
square(5)
square(num=6)
square(int(input()))

# under-construction - making a function that will put emojis in the program on command
# Is working :)

def cats(string_here):
  if string_here == "initiate":
      while 1 < 2:
        newone = input('What do you want to do?(smile, cry, laugh, die)')    
        if newone == 'smile':
          print("😀me too")
          break
        elif newone == 'cry':
          print("😢me too🤧")
          break
        elif newone == 'laugh':
          print("🤣me too!🙊")
          break
        elif newone == "die":
          print("💀me too🔪")
          break
        else:
          print("what?")
  else:
    print('nevermind')
print("Lets see if this works:")
print("Put 'initiate' in the input to initiate the function")
cats(input())
print("\n\nAfter the function, now :")
def square(cube):
  print(cube**3)
square(int(input("Put a number here to get it's cube")))


print("\nEXCEPTIONS:")

try:
    age = int(input("What is your age?"))
    print(f"Your age is {age}")
except ValueError:
    print("Invalid Input")

print("\nCUSTOM EXCEPTIONS :")
class InvalidAge(Exception):
    "Raised when the age is below 18"
    pass

try:
    enternum = int(input("Enter a number here"))
    if enternum < 18:
        raise InvalidAge
    else:
        print("ELigible to vote")
except ValueError:
    print("Invalid Value Entered")
    