'''
Dependency Inversion Principle (DIP):
High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

After separating verification logic payment method class was depeding on certain verification method.
It is better to make abstract class for verification methods.
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


class Verification(ABC):
    @abstractmethod
    def check_status(self) -> bool:
        pass


class SMSVerification(Verification):
    verified = False

    def verify(self, secret_code: str) -> None:
        print(f"Processing code from SMS: {secret_code}")
        self.verified = True

    def check_status(self) -> bool:
        return self.verified


class EmailVerification(Verification):
    verified = False

    def verify(self, secret_code: str) -> None:
        print(f"Processing code from email: {secret_code}")
        self.verified = True

    def check_status(self) -> bool:
        return self.verified


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class CardPaymentProcessor(PaymentProcessor):
    def __init__(self, security_number: str, verification: Verification) -> None:
        self.security_number = security_number
        self.verification = verification

    def pay(self, order: CoffeeShopOrder) -> None:
        if not self.verification.check_status():
            print("verification was not completed!")
            return
        print(f"Paying {order.price} with card for your order")
        print(f"Checking security number: {self.security_number}")
        order.status = "paid"


class OnlinePaymentProcessor(PaymentProcessor):
    def __init__(self, email: str, verification: Verification) -> None:
        self.email = email
        self.verification = verification

    def pay(self, order: CoffeeShopOrder) -> None:
        if not self.verification.check_status():
            print("verification was not completed!")
            return
        print(f"Paying {order.total_price} with card for your order")
        print(f"Checking by email: {self.email}")
        order.status = "paid"


class CashPaymentProcessor(PaymentProcessor):
    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.total_price} with cash for your order")
        order.status = "paid"
