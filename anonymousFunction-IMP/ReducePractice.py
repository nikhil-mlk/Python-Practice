from functools import reduce

#def addValues(a,b):
#    return a+b

ls=[1,2,3,4,5,6]
result=reduce(lambda a,b:a+b,ls)
print(result)


