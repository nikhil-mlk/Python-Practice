from functools import reduce

l=[1,2,3,4,5,6]

list1=list(filter(lambda numb:numb%2==0,l))

list2=list(map(lambda numb:numb+2,list1))

number=reduce(lambda a,b:a+b,list2)

print(number)







