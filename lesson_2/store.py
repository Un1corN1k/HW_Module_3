class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def __bool__(self):
        return bool(self.products)

    def __eq__(self, other):
        return self.products == other.products and self.quantities == other.quantities

    def __float__(self):
        return self.get_total() / 100

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item):
        return [str(self.products[item]), self.quantities[item]]

    def add_product(self, product, quantity) -> None:
        try:
            index = self.products.index(product)
            self.quantities[index] += quantity
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def remove_product(self, product) -> None:
        return self.products.remove(product)

    def sub_product(self, product, quantity) -> None:
        try:
            index = self.products.index(product)
            self.quantities[index] -= quantity
            if self.quantities[index] <= 0:
                self.products.remove(product)
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def get_total(self) -> int:
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.get_total(quantity)
        return total


class PaymentValidator:
    def is_valid(self):
        raise NotImplementedError


class PaymentProcessor:
    def purchase(self, cart):
        return cart.get_total()


class CodeValidator(PaymentValidator):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        print('Card payment processing...')
        password = str(input("Enter your password:"))
        return self.password == password


class CardPaymentProcessor(CodeValidator, PaymentProcessor):
    def purchase(self, cart):
        if self.is_valid():
            return f"Here is your successful payment check for the amount {cart.get_total()/100} UAH"
        else:
            return f'Your payment has not been verified'


class CashValidator(PaymentValidator):
    def is_valid(self):
        return True


class CashPaymentProcessor(CashValidator, PaymentProcessor):
    def purchase(self, cart):
        if self.is_valid():
            print("Cash payment processing...")
            return f"Total bill in the shopping cart {cart.get_total()/100} UAH"


class Product:
    def __init__(self, name: str, price: int, unit: float):
        self.name = name
        self.price = price
        self.unit = unit

    def __str__(self):
        return self.name

    def __float__(self):
        return self.price/100

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit

    def get_total(self, quantity) -> int:
        return round(self.price * (quantity / self.unit))


candy = Product("candy", 1059, 0.1)
juice = Product("juice", 3655, 1)
sweet = Product("sweet", 1589, 0.1)
cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_product(candy, 1)
cart_1.add_product(sweet, 0.5)
cart_1.add_product(juice, 1)
cart_1.add_product(sweet, 0.5)
cart_2.add_product(candy, 2)
cart_2.add_product(juice, 2)
cart_2.add_product(sweet, 0.2)
cart_1.remove_product(candy)
card_processor = CardPaymentProcessor("1234")
card_processor.purchase(cart_1)
cash_processor = CashPaymentProcessor()
cash_processor.purchase(cart_1)
