f1 = open('file1','r')

f2 = open('file3','w')


for data in f1:
    f2.write(data)


