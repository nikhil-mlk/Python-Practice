#       * * * * *
#           *
#           *
#           *
#           *

for k in range(5):
    for i in range(5):
        if k>0 and ((-1<i<2) or i>2):
            print('  ',end='')
        else:
            print('* ', end='')
    print()