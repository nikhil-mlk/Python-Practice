def my_generator(l):
    for i in l:
        yield i




list=[1,2,3,4]

value=my_generator(list)

print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())

