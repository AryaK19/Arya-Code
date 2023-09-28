b =int(input('Enter Your No. : '))

for i in range(2 , b) :
    if(b%i!=0) :
        print('The number is prime')
    else:
        print('The No. is not a prime ')  
    break

