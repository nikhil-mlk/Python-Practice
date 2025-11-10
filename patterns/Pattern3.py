#    * * * * *
#    *       *
#    * * * * *
#    *       *
#    *       *
for k in range(5):
    for i in range(5):
        if (0<k<2 or k>2) and (0<i<4):
            print('  ',end='')
        else:
            print('* ', end ='')
    print()

print('hello', end=' ')
print('nikhil')
print('yatin')

