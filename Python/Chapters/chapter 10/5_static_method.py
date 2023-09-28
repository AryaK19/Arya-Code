class Employee:
    company = 'Google'
    def getSalaryComp(self,signature):
        print(f'Slary for this employee working in {self.company} is {self.salary}\n{signature}')
    
    @staticmethod # it works without "self"
    def greet():
        print('Good Morning, Sir')

arya = Employee()
arya.salary = 100000
arya.getSalaryComp('Thanks') # Employee.getSalary(arya)
arya.greet()# Employee.greet() (kind of gets converted in this format )