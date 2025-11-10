a = 10
b = 20

def showMe():
    globals()['a']=30
    globals()['b']=40
    print(a)
    print(b)

showMe()

