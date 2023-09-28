import math
import matplotlib.pyplot as plt

equation = input("Enter The Equation : y = ")
xaxis = []
yaxis = []
for i in range(-1000,1000):
    x = i
    xaxis.append(x)
    y = eval(equation)
    yaxis.append(y)

plt.plot(xaxis,yaxis)
plt.show()
