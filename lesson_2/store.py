class ShoppingCart:
    name = "none"
    quantity = 0
    total_price = 0

    def add_product(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_total(self):
        self.total_price += Product.get_total(self.name, self.quantity)
        return self.total_price  # працює не коректно, рахує для 1


class Product:
    def __init__(self, name: str, price: int, unit: float):
        self.name = name
        self.price = price
        self.unit = unit

    def __str__(self):
        return self.name

    def __float__(self):
        return float(self.price/100)

    def get_total(self, quantity) -> int:
        return self.price * round(quantity / self.unit)


candy = Product("candy", 1059, 0.1)
juice = Product("juice", 3655, 1)
sweet = Product("candy", 1059, 0.1)
cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_product(candy, 1)
cart_1.add_product(sweet, 0.5)
cart_2.add_product(candy, 2)
cart_2.add_product(juice, 2)
cart_2.add_product(sweet, 0.2)


print(cart_1.get_total())

