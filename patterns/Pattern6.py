for k in range(0,5):
    for i in range(0,5):
        if ((0<k<4 and 0<i<4)) or ((k==0 or k==4) and i==4):
            print('  ',end=' ')
        else:
            print('* ',end=' ')

    print()
