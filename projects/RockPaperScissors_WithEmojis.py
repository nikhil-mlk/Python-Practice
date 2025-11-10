'''
1. System ask user to select rock/paper/scissors (r/p/s)

2. If any other character selected - Wrong input -- > do you want to continue?(y/n)

3. If computer and user input is same --> message: It' s a tie

4. User Win case:
    4.1 user selects paper & computer selects rock
    4.2 user selects scissors & computer selects paper
    4.3 user selects rock & computer selects scissors

5. Do you want to play the game again? ()
'''

import random
import os

bol=True
options=['r','p','s']
emojis={'r':'🥌','p':'📃','s':'✂'}
while bol:

    userInput=input('Select rock/paper/scissors (r/p/s)').lower()
    computerInput=random.choice(options)

    if userInput not in options:
        print(f'You have entered {userInput} which is invalid. Please try again')
    elif userInput==computerInput:
        print(f'You have selected {emojis[userInput]} and computer also selected {emojis[computerInput]} hence it is a tie.')
        playAgainYesOrNo=input('Want to play again (y/n): ').lower()
        if playAgainYesOrNo=='y':
            continue
        else:
            bol=False
    elif (userInput=='p' and computerInput=='r') or (userInput=='s' and computerInput=='p') or (userInput=='r' and computerInput=='s'):
        print(f'You have entered {emojis[userInput]} and computer selected {emojis[computerInput]}. You Win !!!!!')
        bol=False
    else:
        print(f'You have entered {emojis[userInput]} and computer selected {emojis[computerInput]}')
        print('Computer Wins')
        bol=False



