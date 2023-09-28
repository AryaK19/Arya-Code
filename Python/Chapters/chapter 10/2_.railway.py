class RailwayForm:
    formType = 'RailwayForm'
    def printData(self):
        print(f'Name is {self.name}')
        print(f'Train is {self.train}')

aryasApplication = RailwayForm()
aryasApplication.name = "Arya"
aryasApplication.train = "Rajdhani Express"
aryasApplication.printData()
