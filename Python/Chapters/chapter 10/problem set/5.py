# class for train ticket

class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats= seats

    def a(self):
        print(f"The name of the train is {self.name}")
        print(f"The Fare of the train is Rs :{self.fare}")
        print(f"The no.Seat in the train is {self.seats}")

    def bookTicket(self):
        if(self.seats > 0):
            print(f'Your Ticket has been booked ,Your Seat no. is {self.seats}')
            self.seats = self.seats - 1
        else :
            print("You can't Book the Tickets")

    
intercity = Train('Intercity Express 1001',90,2)
intercity.a()
intercity.bookTicket()
intercity.bookTicket()
# intercity.bookTicket()
intercity.a()