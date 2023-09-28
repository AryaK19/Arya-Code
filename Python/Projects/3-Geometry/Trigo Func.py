
#formula 



deg = float(input("Enter x(deg) :"))
rad = (deg*3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094)/180

def Factorial(i):
    b = 1   
    for j in range(1,(i+1)):
        b = b * j
    return b

def Sin(rad):
    vals = 0
    for i  in range(1,100,2):
        vals = (vals + (((-1)**((i+3)/2))*(rad**i))/(Factorial(i)))
    return vals

def Cos(rad):
    valc = 0
    for i  in range(0,100,2):
        valc = (valc + (((-1)**((i+4)/2))*(rad**i))/(Factorial(i)))
    return valc

def Tan(rad):
    return Sin(rad)/Cos(rad)