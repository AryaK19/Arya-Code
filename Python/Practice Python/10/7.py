string = "poppopo"
li = list(string)
for i in range (0, len(string)):
    for j in range (0, len(string)):
        if li[i] == li[len(string) -1 - j]:
            print(li[i:len(string) -1 - j]) 
