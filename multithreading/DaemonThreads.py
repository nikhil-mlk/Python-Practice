from threading import*
from time import sleep

class Hello:
    def method1(self):
        for i in range(5):
            print('Method1')
            sleep(1)

    def method2(self):
        for i in range(5):
            print('Method2')
            sleep(1)

obj = Hello()

t1 = Thread(target=obj.method1,daemon=True)
t2 = Thread(target=obj.method2,daemon=True)

t1.start()
t2.start()

sleep(5)
print('Main Thread Finished')