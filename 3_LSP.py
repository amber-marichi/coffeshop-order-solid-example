'''
Liskov Substitution Principle (LSP):
Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.

To pay with card or online usually it's needed to provide some kind of verification.
To add this functionality means to extend payment method class where it is needed, not modify base class.
So that any payment class derived from base class will work without breaking logic.
'''


from abc import ABC, abstractmethod


class CoffeeShopOrder:
    items = []
    total_price = 0
    status = "open"

    def make_drink(self, drink: str, price: int) -> None:
        self.items.append(drink)
        self.total_price += price
        print(f"Your {drink} is ready!")
    

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class CardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_number: str) -> None:
        self.security_number = security_number

    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with card for your order")
        print(f"Checking security number: {self.security_number}")
        order.status = "paid"


class OnlinePaymentProcessor(PaymentProcessor):
    def __init__(self, email: str) -> None:
        self.email = email
    
    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with card for your order")
        print(f"Checking by email: {self.email}")
        order.status = "paid"


class CashPaymentProcessor(PaymentProcessor):
    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with cash for your order")
        order.status = "paid"
