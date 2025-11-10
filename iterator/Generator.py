def my_generator():
    yield 10
    yield 20
    yield 30
    yield 40

value=my_generator()
print(value.__next__())
print(value.__next__())
print(value.__next__())