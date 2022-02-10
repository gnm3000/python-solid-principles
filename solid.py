
"""[In this ocasion, we apply L Liskov substitution principle]

The Liskov Substitution Principle in practical software development. 
The principle defines that objects of a superclass shall be replaceable
with objects of its subclasses without breaking the application. 
That requires the objects of your subclasses to behave in the same
way as the objects of your superclass

PaypalPaymentProcessor dont work with security_code but with emails
Deberia ser un email address y no securitycode.
El tema que en el abstractmethod es un security_code, y si uso un email en una clase hija
estaria violancio el principio de Liskov

La solucion es quitar el security_code de la funcion y ponerla en la __init__ function


    """
from abc import ABC,abstractmethod

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


class PaymentProcessor(ABC):
    """[We create an abstract PaymentProcessor Class]

    """
    @abstractmethod
    def pay(self,order):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code) -> None:
        self.security_code=security_code
    def pay(self,order):
        print("Processing debit payment type")
        print(f"Verify security code", self.security_code)
        order.status = "paid"
class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code) -> None:
        self.security_code=security_code
    def pay(self,order):
        print("Processing credit payment type")
        print(f"Verify security code", self.security_code)
        order.status = "paid"
class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self,email_address) -> None:
        self.email_address=email_address
    def pay(self,order):
        print("Processing paypal payment type")
        print(f"Verify email address", self.email_address)
        order.status = "paid"

class BitcoinPaymentProcessor(PaymentProcessor):
    def __init__(self,wallet) -> None:
        self.wallet=wallet
    def pay(self,order):
        print("Processing Bitcoin payment type")
        print(f"Verify Wallet", self.wallet)
        order.status = "paid"





order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("gnm3000@gmail.com")
processor.pay(order)
