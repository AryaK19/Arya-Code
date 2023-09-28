Letter = '''Dear, <|NAME|>
You are selected!
Greetings from sir, Arya 
Meeting on 
Date: <|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter the Date\n")
Letter = Letter.replace("<|NAME|>", name)
Letter = Letter.replace("<|DATE|>", date)
print(Letter)