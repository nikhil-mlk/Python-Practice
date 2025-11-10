class Computer:
    def __init__(self,modelNumber,ram):
        self.modelNumber=modelNumber
        self.ram=ram

    def printInformation(self):
        print(self.modelNumber, self.ram)


comp1=Computer('intel i5','16 gb')
comp2=Computer('Celeron','32 gb')

comp1.printInformation()
comp2.printInformation()
















