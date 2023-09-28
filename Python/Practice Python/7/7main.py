# to find determinant of  the matrises

def matrix(m, n):
    o = []
    for i in range(1, m + 1):
        row = []
        for j in range(1, n + 1):
            try:
                inp = int(input(f"Enter  O[{i}][{j}] :"))
            except ValueError:
                print("Number pls....")
                inp = int(input(f"Enter  O[{i}][{j}] :"))
            except UnboundLocalError:
                print("Number pls....")
                inp = int(input(f"Enter  O[{i}][{j}] :"))
            row.append(inp)
        o.append(row)
    return o

def Print(sum):
    for i in range(len(sum)):
        p = print(sum[i])
    return p

def determinant(A):
    if m==3 and n==3:
        a = A[0]
        d1=a[0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        d2=a[1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        d3=a[2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
        d = d1 - d2 + d3
        d=print(f"The Determinant is {d}")
    elif m==2 and n==2:
        a = A[0]
        d1=a[0]*A[1][1]
        d2=a[1]*A[1][0]
        d = d1-d2 
        d=print(f"The Determinant is {d}")
    else:
        d=A[0][0]
        d=print(f"The Determinant is {d}")
    return d

m = int(input("Enter the value of row : "))
n = int(input("Enter the value of column : "))

print("Enter Matix")
A = matrix(m, n)
print("\n")
Print(A)

d = determinant(A)
print("\n")



