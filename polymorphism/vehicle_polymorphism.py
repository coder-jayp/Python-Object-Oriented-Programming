from typing import Union

class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Year must be an integer >= 1886")
        self.brand = brand
        self.model = model
        self.year = year

    def move(self) -> str:
        return f"{self.brand} {self.model} is moving"

    def get_info(self) -> str:
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        super().__init__(brand, model, year)
        if not isinstance(num_doors, int) or num_doors < 2:
            raise ValueError("Number of doors must be an integer >= 2")
        self.num_doors = num_doors

    def move(self) -> str:
        return f"{self.brand} {self.model} drives smoothly with {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, has_sidecar: bool):
        super().__init__(brand, model, year)
        if not isinstance(has_sidecar, bool):
            raise ValueError("has_sidecar must be a boolean")
        self.has_sidecar = has_sidecar

    def move(self) -> str:
        sidecar_text = "with a sidecar" if self.has_sidecar else "without a sidecar"
        return f"{self.brand} {self.model} rides swiftly {sidecar_text}"

if __name__ == "__main__":
    try:
        vehicles = [
            Car("Toyota", "Camry", 2023, 4),
            Motorcycle("Harley-Davidson", "Sportster", 2022, True),
            Vehicle("Generic", "Model X", 2020)
        ]
        
        print("Demonstrating polymorphism with different vehicles:")
        for vehicle in vehicles:
            print(f"- {vehicle.get_info()}: {vehicle.move()}")
    except ValueError as e:
        print(f"Error: {e}")