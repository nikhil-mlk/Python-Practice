from inheritence.ClassA import ClassA
from inheritence.ClassB import ClassB

class ClassC(ClassA,ClassB):
    def method5(self):
        print('I am method 5')

    def method6(self):
        print('I am method 6')

obj1=ClassC()
obj1.method1()
