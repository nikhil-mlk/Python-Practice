class Student:
    school='DAV Model School'

    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def average(self):
        print((self.mark1+self.mark2+self.mark3)/3)

    @classmethod
    def schoolName(cls):
        return cls.school

    @staticmethod
    def classInformation():
        print('This class has methods that calculate average of marks')

s1=Student(23,33,43)
s2=Student(77,88,99)

s1.average()
s2.average()

print(s1.school)
print(s2.school)

print(Student.schoolName())

Student.classInformation()











