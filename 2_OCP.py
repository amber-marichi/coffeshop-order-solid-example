'''
Open/Closed Principle (OCP):
Software entities should be open for extension but closed for modification.

In previos class to add new payment method it was necessary to modify the class itself.
Instead it is possible to make an abstract class and create classes for both paymenth methods.
This way to add new payment method we can simply add new class with its logic and not modify base class.
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
    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with card for your order")
        order.status = "paid"


class CashPaymentProcessor(PaymentProcessor):
    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with cash for your order")
        order.status = "paid"
