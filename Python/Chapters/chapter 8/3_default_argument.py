def greet(name) :
    return print(f'Good day,{name} ')
greet('Arya')

def greet(name = 'Stranger') :
    return print(f'Good day,{name} ')
greet()
greet('Arya')