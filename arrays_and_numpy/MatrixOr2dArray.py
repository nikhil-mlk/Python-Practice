from numpyPractice import*
arr=array([
          [1,2,3,4],[5,6,7,8]
    ])

# ---- Get Dimension of Array 2d, 3d etc ----Method: ndim
print(arr.ndim)

# ---- Get the number of rows and columns in Matrix ---- Method: shape ---(it gives rows and shape in tuple)
print(arr.shape) # Ans: (2,4)

#--- Convert the 2D array into linear or single dimensionla array --- Method:flatten()
# --- It flattens the array ----
arr1=arr.flatten()
print(arr1) # Ans: [1 2 3 4 5 6 7 8]

# ---- Convert 1D array to 2D array ---- Method: reshape(number of rows, number of columns)

arr2=array([1,2,3,4,5,6,7,8,9])
arr3=arr2.reshape(3,3)
print(arr3)

# ---- Print the values in 2-D array ---
arr4=array([
    [1,2,3,4],
    [5,6,7,8],
    [5,2,9,4]
])
for row in range(3):
    for column in range(4):
        print(arr4[row][column],' ',end='')
    print()

# --- Print specific row ----nameOfArray[enterTheRowNumber]
print(arr4[1])

# --- Print specific COLUMN ----nameOfArray[:,enterTheCoumnIndex]
print(arr4[:,1]) # Ans: [2 6 2]

# ----- Adding 2D array ----

arr5=array([
    [1,2,3,4],
    [5,6,7,8],
    [5,2,9,4]
])
arr6=array([
    [1,2,3,4],
    [5,6,7,8],
    [5,2,9,4]
])
print(arr5+arr6)

