from typing import Union
import math

class Shape:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self.name = name

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0

    def get_info(self) -> str:
        return f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, name: str, width: float, height: float):
        super().__init__(name)
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    try:
        shapes = [
            Rectangle("Rectangle 1", 5.0, 3.0),
            Circle("Circle 1", 4.0),
            Shape("Generic Shape")
        ]
        print("Demonstrating polymorphism with different shapes:")
        for shape in shapes:
            print(f"- {shape.get_info()}")
    except ValueError as e:
        print(f"Error: {e}")