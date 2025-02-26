# Write a class Train which has methods to book a ticket, get Status (no of seats) and get fare information of 
# trains running under American Railways.
"""
1 2 3 4 5 6 7 8 9 10
"""
class Train:
    def __init__(self, name, train_name, seats_available):
        self.name = name               
        self.train_name = train_name   
        self.seats_available = seats_available  

    def getStatus(self):
        print(f"Welcome to {self.train_name} train.")
        print(f"Seats available: {self.seats_available}")

    def getFareInfo(self, fare):
        print(f"The fare for {self.train_name} is ${fare} per ticket.")

    def bookTicket(self):
        if self.seats_available > 0:
            print(f"Your ticket has been booked successfully, {self.name}.")
            self.seats_available -= 1
        else:
            print("Sorry! Unfortunately, all seats are booked. Thank you for prioritizing us.")

    def cancelTicket(self):
        print(f"Ticket cancellation requested for {self.name}.")
        self.seats_available += 1
        print(f"Your ticket has been canceled successfully. Updated seat count: {self.seats_available}")



passenger = Train("Palsang", "American Railways", 5)
passenger.getStatus()                                 
passenger.getFareInfo(100)                            
passenger.bookTicket()                                
passenger.getStatus()                                 
passenger.cancelTicket()                              
passenger.getStatus()                                 
