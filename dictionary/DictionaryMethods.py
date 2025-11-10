dict1 = {1:'Nikhil',2:'Vaibhav',3:'Gaurav',4:'Anand'}

# Getting values from Dictionary --> dictionary[key]
print(dict1[2]) # Ans: Vaibhav

# -- if key is not present ----
#print(dict1[6])

print(dict1.get(6))

# Copy Dictionary
dict2 = dict1.copy()
print(dict2)

# List like view of dictionary items
print('Items method:',dict1.items())

# Get ONLY keys
print(dict1.keys()) # Ans: dict_keys([1, 2, 3, 4])

# Get Only Values
print(dict1.values()) # Ans: dict_values(['Nikhil', 'Vaibhav', 'Gaurav', 'Anand'])

# Pop the element using key
#dict1.pop(2)
print(dict1) # Ans: {1: 'Nikhil', 3: 'Gaurav', 4: 'Anand'}

# Pop the last element in dictionary
dict1.popitem()
print(dict1) # Ans: {1: 'Nikhil', 2: 'Vaibhav', 3: 'Gaurav'}


# -- Inserting/adding entries in dictionary
dict2 = {1:'Nikhil',2:'Vaibhav',3:'Gaurav',4:'Anand'}

dict2.__setitem__(5,'Kartik')

dict2.__setitem__(3,'Rahul')
print(dict2)

dict3 = {1:'Nikhil',2:'Vaibhav',3:'Gaurav',4:'Anand'}

dict3.setdefault(5,'Kartik')
print(dict3)

dict4 = {1:'Nikhil',2:'Vaibhav',3:'Gaurav',4:'Anand'}

dict4.setdefault(3,'Kartik')
print(dict4)












