def gr_th_5(num):
    if num > 5 :
        return True
    else  :
        return False

l=[1,2,3,4,5,6,7,89,98]

g10 = lambda num:num>10
# this kind of filters out it 
print(list(filter(gr_th_5,l)))
print(list(filter(g10,l)))