class Train:
    def __init__(self, name, train_name, seat_available):
        self.name = name
        self.train_name = train_name
        self.seat_available = seat_available

    def getStatus(self):
        print(f"Welcome to our {self.train_name}.")
        print(f"Availabel seats are: {self.seat_available}.")

    def fareInfo(self, fare):
        print(f"The price of the {self.train_name} is {fare}.")
    
    def bookTicket(self):
        print("You have requested to book a ticket.")
        if self.seat_available > 0:
            print(f"You have successfully booked your ticket,{self.name}")
            self.seat_available -= 1
        elif self.seat_available == 0:
            print("Sorry, unfortunately there are no seats available.")
        else:
            print("Sorry, unfortunately there are no seats available.")
        

    def cancelTicket(self):
        print(f"Ticket cancellation request for {self.name}")
        self.seat_available += 1
        print(f"Your ticket has been successfully canceled. Updated available seats are: {self.seat_available}")

passenger = Train("Palsang", "New York Metro Station", 2)
passenger.getStatus()
passenger.fareInfo(2000)
passenger.bookTicket()

passenger.getStatus()
passenger.fareInfo(2000)
passenger.bookTicket()

passenger.getStatus()
passenger.fareInfo(2000)
passenger.bookTicket()



