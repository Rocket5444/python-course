'''
Write a class Train which has method to book ticket, get status (no of seats)
and get fare information of train running under Indian railways
'''
from random import radient

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is  {radient(222, 5555)}")

    
t = Train(12399)
t.book("Delhi", "Mumbai")
t.getstatus("Delhi", "Mumbai")
t.getFare("Delhi", "Mumbai")  # This will print a random number