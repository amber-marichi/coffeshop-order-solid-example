'''
Interface Segregation Principle (ISP):
A class should not be forced to implement interfaces it does not use, and clients should not be forced to depend on methods they do not use.

Now it is possible to separate verification functionality into separate class.
This way all payment method classes that need verification via SMS will receive necessary verification class.
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


class SMSVerification:
    verified = False

    def verify(self, secret_code: str) -> None:
        print(f"Processing code from SMS: {secret_code}")
        self.verified = True

    def check_status(self) -> bool:
        return self.verified


class EmailVerification:
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
    def __init__(self, security_number: str, verification: SMSVerification) -> None:
        self.security_number = security_number
        self.verification = verification

    def pay(self, order: CoffeeShopOrder) -> None:
        if not self.verification.check_status():
            print("verification was not completed!")
            return
        print(f"Paying {order.price} with card for your {order.drink_name}")
        print(f"Checking security number: {self.security_number}")
        order.status = "paid"


class OnlinePaymentProcessor(PaymentProcessor):
    def __init__(self, email: str, verification: EmailVerification) -> None:
        self.email = email
        self.verification = verification

    def pay(self, order: CoffeeShopOrder) -> None:
        if not self.verification.check_status():
            print("verification was not completed!")
            return
        print(f"Paying {order.price} with card for your order")
        print(f"Checking by email: {self.email}")
        order.status = "paid"


class CashPaymentProcessor(PaymentProcessor):
    def pay(self, order: CoffeeShopOrder) -> None:
        print(f"Paying {order.price} with cash for your order")
        order.status = "paid"
