class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₹{self.price})"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product, quantity: int = 1):
        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += quantity
        else:
            self.items[product.product_id] = {"product": product, "quantity": quantity}
        print(f"Added {quantity} x {product.name} to the cart.")

    def remove_product(self, product_id: int, quantity: int = 1):
        if product_id in self.items:
            if self.items[product_id]["quantity"] > quantity:
                self.items[product_id]["quantity"] -= quantity
                print(f"Removed {quantity} from {self.items[product_id]['product'].name}")
            else:
                removed_item = self.items.pop(product_id)
                print(f"Removed all of {removed_item['product'].name} from the cart.")
        else:
            print("Product not found in cart.")

    def get_total_price(self):
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nCart contents:")
            for item in self.items.values():
                product = item["product"]
                qty = item["quantity"]
                print(f"{product.name} - ₹{product.price} x {qty} = ₹{product.price * qty}")
            print(f"Total: ₹{self.get_total_price()}\n")

p1 = Product(1, "Laptop", 55000)
p2 = Product(2, "Headphones", 2000)
p3 = Product(3, "Mouse", 800)

cart = Cart()

cart.add_product(p1, 1)
cart.add_product(p2, 2)
cart.add_product(p3, 3)
cart.add_product(p2, 1)

cart.show_cart()

cart.remove_product(2, 1)
cart.show_cart()

print("Final Total:", cart.get_total_price())