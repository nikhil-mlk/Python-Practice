from numpy import *

# Adding 5 to each element in array
arr=array([1,2,3,4,5])
arr=arr+5
print(arr) # Ans : [ 6  7  8  9 10]

# Adding 2 arrays
arr1=array([1,2,3,4,5,6])
arr2=array([1,2,3,4,5,6])
arr3=arr1+arr2
print(arr3) # Ans: [ 2  4  6  8 10 12]

# Square root of all the elements in array
arr4=array([1,2,3,4])
print(sqrt(arr4)) # Ans: [1.         1.41421356 1.73205081 2.        ]

# sum of all the elements in array
print(sum(arr4)) # Ans: 10

# find minimum value in array
print(min(arr4)) # Ans: 1

# find maximum value in array
print(max(arr4)) # Ans: 4

# ---------------- Operations on 2-D array ----------
arr5=array([[1,2,3],[4,5,6]])
print(arr5[0,1]) # Ans: 2 ---> Row : 0 and Column : 1
print(arr5[:,1]) # Ans: [2 5]  --> All rows, Column 1
print(arr5[1,:]) # Ans: [4 5 6] ---> Row 1, all columns

# Concatination of 2 arrays
arr6=array([1,2,3,4])
arr7=array([5,6,7,8])
print(concatenate([arr6,arr7])) # Ans: [1 2 3 4 5 6 7 8]






