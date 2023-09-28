class Person:
    contry = 'India'

    def takeBreath(self):
        print("I am Breathing....")

class Employee(Person) :
    company='Honda'
    salary = 1000000

    def getSalary(self):
        print(f"Salary is {self.salary}")

    @staticmethod
    def takeBreath():
        print("I am an Employee and I am Breathing....")

class Programmer(Employee):
    company = 'Fiverr'

    def getSalary(self):
        print(f"No Salary to Programmers")  

p = Person()
p.takeBreath()
# print(p.company) # Throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr= Programmer()
pr.takeBreath()
print(pr.company)

print(pr.contry)

 