class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.investors = []

    def register_investor(self, investor):
        if investor not in self.investors:
            self.investors.append(investor)
            investor.stocks.append(self)

    def unregister_investor(self, investor):
        if investor in self.investors:
            self.investors.remove(investor)
            investor.stocks.remove(self)

    def update_price(self, price):
        self.price = price
        self.notify_investors()

    def notify_investors(self):
        for investor in self.investors:
            investor.update(self, self.price)

class Investor:
    def __init__(self, name):
        self.name = name
        self.stocks = []

    def update(self, stock, price):
        print(f"{self.name} notified: {stock.symbol} is now {price}")

# Example of usage
def main():
    # Create stock objects
    aapl = Stock('AAPL', 150.00)
    goog = Stock('GOOG', 2800.00)

    # Create investor objects
    john = Investor('Luka')
    jane = Investor('Alikh')

    # Register investors
    aapl.register_investor(john)
    goog.register_investor(jane)
    aapl.register_investor(jane)

    # Update stock prices
    aapl.update_price(155.00)  # Both John and Jane will be notified
    goog.update_price(2900.00)  # Only Jane will be notified

    # Unregister an investor
    aapl.unregister_investor(john)
    aapl.update_price(158.00)  # Only Jane will be notified

if __name__ == "__main__":
    main()
