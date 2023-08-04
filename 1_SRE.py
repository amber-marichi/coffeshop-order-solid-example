''' 
Single Responsibility Principle (SRP):
A class should have only one reason to change.

Class CoffeeShopOrder has two responsibilities and so two reasons to change
It is better to separate payment functionality
'''


class CoffeeShopOrder:
    items = []
    total_price = 0
    status = "open"

    def make_drink(self, drink: str, price: int) -> None:
        self.items.append(drink)
        self.total_price += price
        print(f"Your {drink} is ready!")


class PaymentProcessor:
    def pay_cash(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with cash for your order")
        order.status = "paid"

    def pay_card(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with card for your order")
        order.status = "paid"
