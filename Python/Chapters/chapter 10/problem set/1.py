# create a class programer for sharing information of few programmers woking in microsoft

class Programmer:
    company = 'Microsoft'
    def __init__(self,name,product) :
        self.product = product
        self.name = name
    def getInfo(self):
        print(f"Name of the programmer is {self.name} and working on {self.product}")

arya = Programmer('Arya',"Skype")
harry = Programmer('Harry','GitHub')
arya.getInfo()
harry.getInfo()
        
        