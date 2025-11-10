#from abc import ABC, abstractmethod
from abc import*

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    def cashPayment(self):
        print('Cash Payment Not allowed')

class CreditCard(Payment):
    def pay(self):
        print('This is credit card payment')

class Upi(Payment):
    def pay(self):
        print('This is UPI payment')


obj1=CreditCard()
obj1.pay()
obj1.cashPayment()



