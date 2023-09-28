text = input("Enter the text : ")
spam = False

if('make a lot of money'in text ) :
    spam = True
elif('buy now'in text) :
    spam = True 
elif('watch this'in text) :
    spam = True
else :
    spam = False 
if spam:
    print('The text is a spam')
else :
    print('The text is not a spam')
