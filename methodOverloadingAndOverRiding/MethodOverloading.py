class Calculator:
    def addition(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        elif a!=None:
            print('Only 1 number is entered')

obj1 = Calculator()

obj1.addition(3,3,3) # Ans: 9
obj1.addition(3,3) # Ans: 6
obj1.addition(3) # Ans: Only 1 number is entered



