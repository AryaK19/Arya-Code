class Person:
    contry = 'India'

    def takeBreath(self): 
        print("I am Breathing....")

class Employee(Person) :
    company='Honda'
    salary = 1000000

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee and I am Breathing....")

class Programmer(Employee):
    company = 'Fiverr'

    def getSalary(self):
        print(f"No Salary to Programmers")  

p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr= Programmer()
pr.takeBreath()

 