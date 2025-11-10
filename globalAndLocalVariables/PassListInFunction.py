def evenAndOdd(ls):
    listEven=[]
    listOdd=[]
    for i in ls:
        if i%2==0:
            listEven.append(i)
        if i%2!=0:
            listOdd.append(i)
    return listEven,listOdd



l=[1,2,3,4,5,6]
lsEven,lsOdd=evenAndOdd(l)
print(lsEven)
print(lsOdd)









