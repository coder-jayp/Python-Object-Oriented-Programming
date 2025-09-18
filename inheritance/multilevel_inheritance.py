class Vehicle:
    def move(self):
        print("This vehicle can move.")

class Car(Vehicle):
    def wheels(self):
        print("This car has 4 wheels.")

class ElectricCar(Car):
    def fuel(self):
        print("This car runs on electricity.")

tesla = ElectricCar()
tesla.move()    
tesla.wheels()  
tesla.fuel()  
