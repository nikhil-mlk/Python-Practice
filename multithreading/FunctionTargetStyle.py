from threading import *
from time import sleep

def hello():
    for i in range(5):
        print('Hello')
        sleep(1)
def hi():
    for k in range(5):
        print('Hi')
        sleep(1)

t1 = Thread(target=hello)
t2 = Thread(target=hi)

t1.start()
t2.start()

t1.join()
t2.join()

print('Main Program Finished')



