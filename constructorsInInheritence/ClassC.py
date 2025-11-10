from constructorsInInheritence.ClassA import ClassA
from constructorsInInheritence.ClassB import ClassB

class ClassC(ClassA,ClassB):

    def __init__(self):
        super().__init__()
        print('Class C Init Constructor')

    def method5(self):
        print('I am method 5')

    def method6(self):
        print('I am method 6')

obj1=ClassC()

