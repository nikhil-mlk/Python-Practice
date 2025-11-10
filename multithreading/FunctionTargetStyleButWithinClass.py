from threading import*
from time import sleep

class Hello:
    def method1(self):
        for i in range(10):
            print('Hello')
            sleep(1)
    def method2(self):
        for k in range(10):
            print('Hi')
            sleep(1)

obj = Hello()

t1 = Thread(target=obj.method1)
t2 = Thread(target=obj.method2)

t1.start()
t2.start()

t1.join()
t2.join()



