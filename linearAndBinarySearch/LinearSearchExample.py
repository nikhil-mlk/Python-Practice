def searchANumber(lst,numb):
    indexValue = -1
    for i in range(len(lst)):
        if lst[i]==numb:
            indexValue=i
            print('Index Value of ',numb,' is:',indexValue)
            return True
    return False

ls=[6,3,5,8,9,2,4]

result=searchANumber(ls,99)
print(result)
