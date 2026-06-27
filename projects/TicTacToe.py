from numpyPractice import *

arr = array([['1','2','3'],
             ['4','5','6'],
             ['7','8','9']])

p1='X'
p2='O'

def showBoard():
    print(arr)

def player1Choice():
    choice1=str(input('Player 1 enter your choice: '))
    return choice1

def player2Choice():
    choice2=str(input('Player 2 enter your choice: '))
    return choice2

def searchChoice(choice,player):
    for i in range(3):
        for j in range(3):
            if arr[i][j]==choice:
                arr[i][j]=player

def checkWinner():
    if((arr[0][0]=='X' and arr[0][1]=='X' and arr[0][2]=='X') or (arr[1][0]=='X' and arr[1][1]=='X' and arr[1][2]=='X') or (arr[2][0]=='X' and arr[2][1]=='X' and arr[2][2]=='X')\
            or (arr[0][0]=='X' and arr[1][0]=='X' and arr[2][0]=='X') or (arr[0][1]=='X' and arr[1][1]=='X' and arr[2][1]=='X')\
            or (arr[0][2]=='X' and arr[1][2]=='X' and arr[2][2]=='X')
            or (arr[0][0]=='X' and arr[1][1]=='X' and arr[2][2]=='X')
            or (arr[0][2]=='X' and arr[1][1]=='X' and arr[2][0]=='X')):
        print('Player A Wins !!!')
        return True

    elif((arr[0][0]=='O' and arr[0][1]=='O' and arr[0][2]=='O') or (arr[1][0]=='O' and arr[1][1]=='O' and arr[1][2]=='O') or (arr[2][0]=='O' and arr[2][1]=='O' and arr[2][2]=='O') \
         or (arr[0][0]=='O' and arr[1][0]=='O' and arr[2][0]=='O') or (arr[0][1]=='O' and arr[1][1]=='O' and arr[2][1]=='O') \
         or (arr[0][2]=='O' and arr[1][2]=='O' and arr[2][2]=='O')
         or (arr[0][0]=='O' and arr[1][1]=='O' and arr[2][2]=='O')
         or (arr[0][2]=='O' and arr[1][1]=='O' and arr[2][0]=='O')):
        print('Player B Wins !!!')
        return True


result=True
count=0
while(result or count<9):
    showBoard()
    print()

    ch1=player1Choice()
    searchChoice(ch1,p1)
    showBoard()

    res=checkWinner()
    if res==True:
        result=False
        break

    ch2=player2Choice()
    searchChoice(ch2,p2)
    showBoard()

    res=checkWinner()
    if res==True:
        result=False
        break

    count=count+1





































