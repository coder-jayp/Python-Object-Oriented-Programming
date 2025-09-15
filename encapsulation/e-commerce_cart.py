class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, item, price):
        self.__items[item] = price 
        print(f"Added: {item} ${price}")
    
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"{item} not in cart")

    def view_cart(self):
        if not self.__items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item, price in enumerate(self.__items.items(), 1):
                print(f"{item}. {price}")
    
    def checkout(self):
        if not self.__items:
            print("cart is empty. Nothing to checkpoint")
            return
        self.view_cart()
        total = sum(self.__items.values())
        print(f"The total price is: {total}")
        self.__items.clear()
        print(f"checkout complete. cart is empty")

cart = ShoppingCart()
cart.add_item("Laptop", 100000)
cart.add_item("phone", 35000)

cart.view_cart()
cart.checkout()
cart.view_cart()