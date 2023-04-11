class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def __bool__(self):
        if self.products == [] and self.quantities == []:
            return False
        else:
            return True

    def __eq__(self, other):
        return self.products == other.products and self.quantities == other.quantities

    def __ne__(self, other):
        return self.products != other.products and self.quantities != other.quantities

    def __float__(self):
        return self.get_total() / 100

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item):
        return [str(self.products[item]), self.quantities[item]]

    def add_product(self, product, quantity):
        self.products.append(product)
        self.quantities.append(quantity)

    def get_total(self):
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
        if self.password == password:
            return True
        else:
            print("Try another password")


class CardPaymentProcessor(CodeValidator, PaymentProcessor):
    def purchase(self, cart):
        if self.is_valid():
            return f"Here is your successful payment check for the amount {cart.get_total()/100} UAH"
        else:
            return f'Your payment has not been verified'


class CashValidator(PaymentValidator):
    def is_valid(self):
        return "Cash payment processing..."


class CashPaymentProcessor(CashValidator, PaymentProcessor):
    def purchase(self, cart):
        print(self.is_valid())
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

    def get_total(self, quantity) -> int:
        return round(self.price * (quantity / self.unit))


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
card_processor = CardPaymentProcessor("1234")
card_processor.purchase(cart_1)
cash_processor = CashPaymentProcessor()
cash_processor.purchase(cart_1)

# print(str(juice))
# print(float(juice))
# print(cart_1.get_total())
# print(float(cart_1))
# print(bool(cart_1))
# print(cart_1 == cart_2)
print(len(cart_2))
print(cart_1[0])

