from numpyPractice import*
# Suppose you have one array. Now you want to copy that array and create another array out of it

arr1=array([1,2,3,4,5,6])

# Method 1:
arr2=arr1

print(arr1)
print(arr2)

print(id(arr1)) # Print Address of arr1 in memory
print(id(arr2)) # Print Address of arr2 in memory


# Case 2: If you want 2 Copy array BUT this time you want two seprate arrays ----> view() method is used
arr3=array([1,2,3,4,5,6])
arr4=arr3.view()

print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))

# ----- Continue Case 2: ---> concept of shallow copy
arr3=array([1,2,3,4,5,6])
arr4=arr3.view()


arr3[1]=55

print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))

# Case 3: --- Deep copy ----
arr5=array([1,2,3,4,5,6])
arr6=arr5.copy()

arr5[2]=77

print(arr5)
print(arr6)

print(id(arr5))
print(id(arr6))





