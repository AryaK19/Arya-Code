code = 3

sta_dic = {}

def word_dic():
    return {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26,
        " " : 28,
        "0" : 29,
        "1" : 30,
        "2" : 31,
        "3" : 32,
        "4" : 33,
        "5" : 34,
        "6" : 35,
        "7" : 36,
        "8" : 37,
        "9" : 38,
    }

def ran(code):
    items = list(sta_dic.items())
    for i in range(0,len(statment_list)):
        for j in range(0,len(items)):
            try:
                value = items[j].index(statment_list[i])
                
            except ValueError:
                value = 0

            if value == 1 and items[j][1] <= 20:
                statment_list[i] = items[j][1]  + (i+1)

            elif value == 1 and items[j][1] > 20 :
                
                statment_list[i] = items[j][1] - (i+1)
    print(statment_list)
            

def decode():
    COtoRan()
    items = list(sta_dic.items())
    # print(items)
    for i in range(0,len(statment_list)):
        for j in range(0,len(items)):
            try:
                value = items[j].index(statment_list[i])
                
            except ValueError:
                value = 0

            if value == 1 and items[j][1] <= 20:
                statment_list[i] = (items[j][1] + (i+1))
                statment_list[i] = statment_list[i]
                

            elif value == 1 and items[j][1] > 20:
                statment_list[i] = (items[j][1] - (i+2))
                
                
    print((statment_list))        

def RANtoCO():
    items = list(sta_dic.items())
    # print(items)
    for i in range(0,len(statment_list)):
        for j in range(0,len(items)):
            try:
                value = items[j].index(statment_list[i])
                
            except ValueError:
                value = 0

            if value == 1 :
                statment_list[i] = items[j][0]



def COtoRan():
    for i in range(0,len(statment)):
        print(statment_list[i],end="")
        statment_list[i] = sta_dic[statment_list[i]]  



statment = input("INPUT:\n")

sta_dic = word_dic()

statment_list = list(statment.lower())

print(statment_list)  

COtoRan()
    
statment_lists = statment_list
print(statment_list)  

ran(code)
RANtoCO()
decode()  

# decode(code)


 