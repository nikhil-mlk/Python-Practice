a = 10
b = 20

def showMe():

    globals()['a']=88
    globals()['b']=99
    print('In showMe function: ',a)
    print('In showMe function: ',b)

showMe()

print('Global value of a: ',a)
print('Global value of b: ',b)

