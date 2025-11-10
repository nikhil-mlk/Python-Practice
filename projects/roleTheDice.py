'''
Ask user if he wants to play if user says yes then select 2 random numbers between 1-6 and show numbers to user
'''


import random
def rollDice():
        ls=[1,2,3,4,5,6]
        responce = str(input('Do you want to roll the dice?: y or n :'))
        choice = responce.lower()
        if choice == 'n':
            print('Thank you for playing the game')
        elif choice!='n' and choice!='y':
            print('Invalid input')
        else:
            lsDiceValue=random.choices(ls,k=2)
            print(lsDiceValue)
rollDice()


