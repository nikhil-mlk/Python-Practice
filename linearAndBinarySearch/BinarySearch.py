def binarySearch(lst,number):
    lowerBound=0
    upparBound=len(lst)-1
    midValue=0

    while lowerBound<=upparBound:

        midValue = (int(lowerBound+upparBound)//2)

        if lst[midValue]==number:
            print('Number',number,' is at index',midValue)
            break

        elif number>lst[midValue]:
            lowerBound=midValue

        elif number<lst[midValue]:
            upparBound=midValue


ls=[4,7,8,12,45,99]
binarySearch(ls,8)
