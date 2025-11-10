from array import*

arr=array('i',[])
numberOfDigitsUserWantToEnter=int(input('How many numbers you want to enter in the array: '))

for j in range(numberOfDigitsUserWantToEnter):
    value=int(input('Enter the value: '))
    arr.append(value)
print(arr)


valueToSearch=int(input('Enter the value you want to search: '))

# Method 1 to search value in array and get its index
inc=0
for k in arr:
    if k==valueToSearch:
        print(inc)
        break
    inc+=1

# Method 2 to search value in array and get its index (using predefined method)
print(arr.index(valueToSearch))
