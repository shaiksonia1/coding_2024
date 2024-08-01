from random import randint
class Train:
    def __init__(self,trainNo) :
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in trainNo {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"train  is running on time {self.trainNo}")

    def getFare(self,fro, to):
        print(f"Ticket is fare for trainNo {self.trainNo} from {fro} to {to} is {randint(222,5555)}")


t = Train(4545)
t.book("delhi","hyderabad")
t.getStatus()
t.getFare("delhi","hyderabad")