d1 = {
   "pankha" : "fan",
   "dhool" : "dust",
   "dabba": "box"
}
print("Options are",list(d1.keys()))
a = input("Enter the Hindi word\n") 
print("the meaning of your word is :", d1.get(a))# get will not show error