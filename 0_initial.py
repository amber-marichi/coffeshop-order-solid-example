'''
basic class that represents the order in coffee shop
make_drink adds new drink to the order list and increasing total price
pay method gives 2 options to pay - with cash and with card
'''


class CoffeeShopOrder:
    items = []
    total_price = 0
    status = "open"

    def make_drink(self, drink: str, price: int) -> None:
        self.items.append(drink)
        self.total_price += price
        print(f"Your {drink} is ready!")

    def pay(self, payment_method: str) -> None:
        if payment_method == "cash":
            print("Processing payment with cash")
            self.status = "paid"
        elif payment_method == "card":
            print("Processing payment with card")
            self.status = "paid"
        else:
            print("Error! this payment method is not supported")
