from array import*

# case 2:
arr1=array('i',[])
numberOfValuesToEnter=int(input('How many values you want to enter: '))
for k in range(numberOfValuesToEnter):
    userValue=int(input('Enter the value: '))
    arr1.append(userValue)
print(arr1)

numberToSearch=int(input('Enter the number for which you want index: '))
if numberToSearch in arr1:
    print(f'Index of {numberToSearch} is: ',arr1.index(numberToSearch))
else:
    print('Number is not present in array')














