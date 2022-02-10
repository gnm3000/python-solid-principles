
"""[D Dependency Inversion]
# We want to depends of abstraction, and not in concrete subclasses
# here payment processes, are depending in specific authrizers.
# Create other abstract authorizer class that you
# pass to payment process
# NOW we are going to create another autorization method
    """


from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):

    authorized = False

    def verify_code(self, code):
        print(f"Verify code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print(" Are you a robot? Naa")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    """[We create an abstract PaymentProcessor Class]

    """
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer) -> None:
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if(not self.authorizer.is_authorized()):
            raise Exception("Not Authorized")

        print("Processing debit payment type")
        print("Verify security code", self.security_code)
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code) -> None:
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print("Verify security code", self.security_code)
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer) -> None:
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if(not self.authorizer.is_authorized()):
            raise Exception("Not Authorized")
        print("Processing paypal payment type")
        print("Verify email address", self.email_address)
        order.status = "paid"


class BitcoinPaymentProcessor(PaymentProcessor):
    def __init__(self, wallet) -> None:
        self.wallet = wallet

    def pay(self, order):
        print("Processing Bitcoin payment type")
        print("Verify Wallet", self.wallet)
        order.status = "paid"


order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())

authorizer = NotARobot()

processor = PaypalPaymentProcessor("gnm3000@gmail.com", authorizer=authorizer)
authorizer.not_a_robot()
# this works because we made sure that the authorizer is a tyoe of authorizer.
processor.pay(order)
