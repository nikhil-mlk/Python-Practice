# We have list and we need to find if the number in the list is divisible by 5. If yes then return the number else return text : Number Not found

list=[2,3,4,16,17]

for i in list:
    if(i%5==0):
        print(i)
        break
else:
    print('Number Not found')
