list1 = [3,53,2,False,6.2,"Arya"]

index=0

for item in list1:
    print(item,index)
    index +=1

#or you can write this 

# ___________________________________________________________________________#
print("---")
# ___________________________________________________________________________#

#index,item,ect
for index,item in enumerate(list1):
    print(item,index)