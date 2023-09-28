# Inheritance is a way of creating  a new class from exiting one 

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language= 'Python'           
    def getName(self,language):
        self.language=language
        print(f"The LAnguage is {self.language}")

    def showDetails(self):
        print("This is an Programmer")
        
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)




