# to find addition of two matrises


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


def sum(A, B):
    new = []
    for i in range(len(A)):
        l = []
        varA = A[i]
        varB = B[i]
        for j in range(len(B)):
            l.append(varA[j] + varB[j])
        new.append(l)
    return new


def Print(sum):
    for i in range(len(sum)):
        p = print(sum[i])
    return p


m = int(input("Enter the value of row : "))
n = int(input("Enter the value of column : "))

print("Enter Matix A")
A = matrix(m, n)
Print(A)
print("\n")

print("Enter Matix B")
B = matrix(m, n)
Print(B)
print("\n")

sum = sum(A, B)

print("The sum of A and B matries is :")
Print(sum)
