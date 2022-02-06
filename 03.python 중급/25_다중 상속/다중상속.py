
class Car01:
    def drive(self):
        print('drive')

class Car02:
    def turbo(self):
        print('turbo')

class Car03:
    def fly(self):
        print('fly')

class Car(Car01, Car02, Car03):
    def __init__(self):
        pass

mycar = Car()

mycar.drive()