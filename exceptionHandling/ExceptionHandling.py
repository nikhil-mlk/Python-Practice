
denominator=int(input('Enter the number:'))
numerator=6

try:
    result=numerator/denominator
    print(result)
except Exception as e:
    print('You Cant divide by 0')
    print(e)




