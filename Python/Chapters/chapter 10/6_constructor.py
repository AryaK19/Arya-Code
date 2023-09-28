# __int__() Constructor

''' it is a speacial method which is first 
run as soon as the object is created'''

# it takes "self" argument

# it runs automatically


class Employee:
    company = 'Google'

    def __init__(self,name,salary,subunit) :
        self.name = name
        self.salary = salary
        self.subunit = subunit

        print('Employee is Created')

    def getDetails(self):
        print(f'The Name of the Employee is {self.name}')
        print(f'The Salary of the Employee is {self.salary}')
        print(f'The Subunit of the Employee is {self.subunit}')

    def getSalaryComp(self,signature):
        print(f'Slary for this employee working in {self.company} is {self.salary}\n{signature}')
    
    @staticmethod 
    def greet():
        print('Good Morning, Sir')

arya = Employee('Arya',100,"Youtube")
arya.getDetails()