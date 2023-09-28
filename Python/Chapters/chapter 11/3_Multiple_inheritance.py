class Employee:
    company='Visa'
    ecode = 120

class Freelancer:
    company = 'Fiverr'
    level = 0

    def upgradelevel(self):
        self.level=self.level +1 

class Programmer(Employee,Freelancer):# if employe write first it will have priority
    name = 'Rohit'

p = Programmer()
p.upgradelevel()
print(p.level)
print(p.company)