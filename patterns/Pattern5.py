#       * * * * *
#           *
#           *
#           *
#           *

for k in range(5):
    for i in range(5):
        if -1<k<5 and ((0<i<4) or (i==4)):
            print('  ',end='')
        else:
            print('* ', end='')
    print()