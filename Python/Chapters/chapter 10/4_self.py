class Employee:
    company = 'Google'
    #if self not used throws an error
    #by using self you can use instance and class atribute
    def getSalaryComp(self):
        print(f'Slary for this employee working in {self.company} is {self.salary}')

arya = Employee()
arya.salary = 100000
arya.getSalaryComp() # Employee.getSalary(arya)
