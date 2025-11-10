from inheritence.Nikhil import Nikhil

class Pawan(Nikhil):

    def __init__(self):
        super().__init__()
        print('This is Pawan class constructor')

    def pawanMethod(self):
        print('This is Pawan class method')

obj1 = Pawan()
