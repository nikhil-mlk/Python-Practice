def simple_exception():
    denominator = int(input('Enter the number:'))
    numerator = 6

    try:
        result = numerator / denominator
        print(result)
    except Exception as e:
        print('You Cant divide by 0')
        print(e)



def user_is_throwing_exception():
    age=int(input('Enter the age:'))
    if age<18:
        raise Exception('You cant vote')

user_is_throwing_exception()






