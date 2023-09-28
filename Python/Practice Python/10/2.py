sum = int(input("Enter Value : "))
add = False
n = [5,7,1,2,8,4,3]

for num in n:
    for nums in n:
        if (num + nums) == sum and num != nums and num > nums:
            print(num,'+',nums,'=',sum)
            add = True
if not add : 
    print("No Number Adds to",sum)
