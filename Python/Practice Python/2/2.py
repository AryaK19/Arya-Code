# part 1 - Calculate the factorial of the given no.
# part 2 - Calculate the no.of Trailing zeros in that factorial

# Parth - 1
a = int(input("Enter a number : "))
c=1
for i in range (1,a+1):
    c=i*(c)

print(f"The Factorial of the no. is {c}")

# Part - 2
#ok just realized this  is a hard one !!

# zeros=str(c).count('0')#
# print(f"The no. of Trailing Zeros is {zeros}")#

c=list(str(c))


for i in range(1,len(c)+1):
    no = -i 
    if c[no]!='0':
        break
    else:
        continue
        

print(f"The no. of Trailing Zeros is {i-1}")
