class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting....")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping....")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def open_doors(self):
        print(f"{self.brand} {self.model} has {self.doors} doors open.")

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        
    def doing_wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie....")

c = Car("toyota", "Corolla", 2)
c.start()
c.open_doors()

b = Bike("honda", "splender")
b.start()
b.doing_wheelie()