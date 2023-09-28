class Employee:
    company = 'Google'
    salary = 100

arya = Employee()
partha = Employee()
#creating instance atribute
arya.salary= 300
partha.salary=400

print(arya.company)
print(partha.company)
Employee.company = 'Youtube'
print(arya.company)
print(partha.company)
print(arya.salary)
print(partha.salary)

print()