from operator import index

import pandas as pd


df=pd.read_excel('student_data.xlsx')

#print(df)

#print(df['Name_of_Student']=='Yash Reddy')

#  df.loc[row,column]
#print(df.loc[3])


# Extract value of a column for specific row
# print(df.loc[3,'Social'])
# print(type(df.loc[3,'Social']))

# Extract Multiple values of a column for specific row
# print(df.loc[3,['English','Social','Physics']])
# print(type(df.loc[3,['English','Social','Physics']]))


#Print the row in which name is Arjun Patel
#print(df.loc[df['Name_of_Student']=='Arjun Patel'])

# For row number 3 print columns from Social to Biology
#print(df.loc[3,'Social':'Biology'])

# Print all rows but only English and Math columns
#print(df.loc[:,['English','Math']])

# Row
print(df.iloc[4,0:2])





































