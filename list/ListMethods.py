# --- Declare List -----
list1=[1,2,3,4,5,6,7,8]
print(list1)

# --- Get value from List ------> list[index]
list2=[1,2,3,4,5,6,7,8]
print("List 2: ",list2[0])

# --- Get value from List ------> from start index TO end Index
print("List from index 2 to 5:",list2[2:6]) # [3, 4, 5, 6]

# --- Adding value in List (At LAST in list)---> append(value)
list3=[1,2,3,4,5,6,7,8]
list3.append(9)
print(list3)  # Ans: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#--- Adding value in List (At SPECIFIC index)---> insert(index,value)
list4=[1,2,3,4,5,6,7,8]
list4.insert(1,100)
print(list4) # [1, 100, 2, 3, 4, 5, 6, 7, 8]

# --- Adding Multiple values in List ---> list.extend([list of items]) ---> Imp
list8=[1,2,3,4,5,6,7,8]
list8.extend([9,10,11])
print("Extended List: ",list8) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# --- Remove value from list ---- remove value by name ---> remove(valueToRemove)
list5=[1,2,3,4,5,6,7,8]
list5.remove(3)
print(list5) # [1, 2, 4, 5, 6, 7, 8]

# --- Remove value from list ---- remove value at certain index ---> del listName[index]
list6=[1,2,3,4,5,6,7,8]
del list6[2]  # value at index 2 will be deleted
print(list6) # [1, 2, 4, 5, 6, 7, 8]

# --- del also remove the list from the memory. It is different from clear.
# In clear, list is still present but empty BUT in del there will be no list
ls=[1,2,3,4,5]
del ls

# --- Remove value from list ---- remove LAST value in list ---> pop()
list7=[1,2,3,4,5,6,7,8]
list7.pop()
print(list7) # [1, 2, 4, 5, 6, 7]

# --- Update Values in List ---> change value at index --- list[index]=value
list9=[1,2,3,4,5,6,7,8,9]
list9[1]=100 # This will update value at index 1 and update it to 100
print(list9)

# ---- Get FIRST INDEX of value  ---- list.index(value)
list10=[1,2,3,4,5,6,3,8,9,3]
print(list10.index(3)) # ans : 2

# --- count the occurance of value --- list.count(value)
print(list10.count(3)) # Ans: 3

# ---- Sum of all values in List ---> sum(list)
list11=[1,2,3,4]
print(sum(list11)) # 10

# ---- Maximum in List --- > max(list)
list12=[1,2,3,56,2,3,4,88,2,4,66]
print(max(list12)) # 88

# ---- Minimum in List --- > min(list)
print(min(list12)) # 1

# --- Sort the list ---
list13=[4,6,1,7,2]
print(list13.sort())

'''
 ---- Copy the lists ---
 There are 2 methods:
 
 Method1:
 Suppose we have ls_2=ls_1
 In this case ls_2 is a reference of ls_1. The problem is if we make any change in ls_1, the same
 change will reflect in ls_2
 
 Suppose we dont want this then opt method 2
 
 Method 2: Use copy() method 
 In this method once we copy the existing list to other. After that even if we make any changes
 in the first list, it will not impact other
 '''
# Copy lists
ls_1=['a','b','c','d','e']
ls_2=ls_1

ls_1.append('k')
print(ls_2)

# Use of copy method
fruits=['apple','banana','pear']
fruits_1=fruits.copy()

fruits.append('mango')
print(fruits_1)




















