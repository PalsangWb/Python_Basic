class PlaneTicket:
    formType = "PlaneTicket"
    def printReport(anything):
        print(f"Name = {anything.name}")
        print(f"Plane = {anything.plane}")

passengerApplication = PlaneTicket()
passengerApplication.name = "Palsang"
passengerApplication.plane = "F-15 Eagle"
passengerApplication.printReport()

