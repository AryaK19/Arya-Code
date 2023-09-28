print("CLASSES IN PYTHON")
print("Classes can be used to form Custom Exceptions")

#Creating an empty class

class A:
    pass
obj1 = A()

class B:
    age = 18
    print(age)
obj2 = B()
#Constructor was not specified here. There was a constructor put there by the interpreter automatically

class C:
    def __init__(self):
        age = 10
        print(age)
obj3 = C()
obj4 = C()

print()

class D:
    age = 20
    print(age)
obj5 = D()
print(obj5.age)
print(D.age)

print("\n")

class Room:
    def calculate_area(self):
        return self.length * self.breadth
thisroom = Room()
thisroom.length = 40
thisroom.breadth = 40

Room.calculate_area(thisroom)
print("Why isn't this working?")

# class Bike:
#     # Constructor Function
#     def __init__(self, Name = ""):
#         self.name = Name

#         return f"{Name} is a nice bike"

# kawasaki = Bike("Ninja")
# Check what is wrong here
# Error on Colab - __init__() should return None, not 'str'


print("\nINHERITANCE")

class Animal:
    def eat(self):
        print("This one can eat")
    def walk(self):
        print("This one can walk")

class Dog(Animal):
    def eat(self):
        print("This one likes to eat jelly")

class Cat(Animal):
    pass

labrador = Dog()
pussy = Cat()
labrador.eat()
labrador.walk()
print("\n")
pussy.walk()
pussy.eat()

# WHAT IS THIS STUPID ERROR?