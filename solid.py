
"""[In this ocasion, we aply O - Open/Close]
Be able to extend code with new functionality
but close for modification, we shouldn't need to modify existing code

The issue is if I need add bitcoin payment, i need to modify PaymentProcessor
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
    def pay(self,order,security_code):
        pass
    
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing debit payment type")
        print(f"Verify security code", security_code)
        order.status = "paid"
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing credit payment type")
        print(f"Verify security code", security_code)
        order.status = "paid"
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing paypal payment type")
        print(f"Verify security code", security_code)
        order.status = "paid"

class BitcoinPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing Bitcoin payment type")
        print(f"Verify security code", security_code)
        order.status = "paid"





order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
processor = BitcoinPaymentProcessor()
processor.pay(order, "999")
