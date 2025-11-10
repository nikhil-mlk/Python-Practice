class Car:
    wheels = 4
    def __init__(self):
        self.company='BMW'
        self.color='White'

car1 = Car()
car2 = Car()

car1.company='Audi'

Car.wheels=6

print(car1.company,car1.color,car1.wheels)
print(car2.company,car2.color,car2.wheels)

 