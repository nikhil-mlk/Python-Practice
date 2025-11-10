#  def employee(name,age):
#      print(name)
#      print(age-5)
#
#  employee(age=30,name='Nikhil')

#  def employee(name,age=18):
#      print(name)
#      print(age)
#
#  employee('Nikhil',44)

def addNumbers(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

addNumbers(3,4,5,6)





