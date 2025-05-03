class StockPortfolio:
    def _init_(self):
        """Initializes an empty stock portfolio."""
        self.portfolio = {}  # Dictionary to store stocks: {ticker: {'shares': int, 'avg_buy_price': float}}

    def buy_stock(self, ticker, shares, price):
        """Adds a stock to the portfolio or increases existing shares."""
        if ticker in self.portfolio:
            existing_shares = self.portfolio[ticker]['shares']
            existing_avg_price = self.portfolio[ticker]['avg_buy_price']
            total_value = existing_shares * existing_avg_price + shares * price
            total_shares = existing_shares + shares
            self.portfolio[ticker]['shares'] = total_shares
            self.portfolio[ticker]['avg_buy_price'] = total_value / total_shares
        else:
            self.portfolio[ticker] = {'shares': shares, 'avg_buy_price': price}
        print(f"Bought {shares} shares of {ticker} at ${price:.2f}")

    def sell_stock(self, ticker, shares, price):
        """Sells shares of a stock from the portfolio."""
        if ticker not in self.portfolio:
            print(f"You don't own any shares of {ticker}.")
            return

        if shares > self.portfolio[ticker]['shares']:
            print(f"You only own {self.portfolio[ticker]['shares']} shares of {ticker}. Cannot sell {shares}.")
            return

        self.portfolio[ticker]['shares'] -= shares
        print(f"Sold {shares} shares of {ticker} at ${price:.2f}")

        if self.portfolio[ticker]['shares'] == 0:
            del self.portfolio[ticker]
            print(f"All shares of {ticker} sold. Removed from portfolio.")

    def view_portfolio(self):
        """Displays the current stock portfolio."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\n--- Your Portfolio ---")
        for ticker, holding in self.portfolio.items():
            print(f"Ticker: {ticker}, Shares: {holding['shares']}, Avg. Buy Price: ${holding['avg_buy_price']:.2f}")
        print("----------------------\n")

def main():
    """Main function to interact with the stock portfolio tracker."""
    my_portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker Menu:")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker symbol: ").upper()
            try:
                shares = int(input("Enter number of shares to buy: "))
                price = float(input("Enter the buying price per share: "))
                if shares > 0 and price > 0:
                    my_portfolio.buy_stock(ticker, shares, price)
                else:
                    print("Shares and price must be positive values.")
            except ValueError:
                print("Invalid input. Please enter numbers for shares and price.")

        elif choice == '2':
            ticker = input("Enter stock ticker symbol to sell: ").upper()
            try:
                shares = int(input("Enter number of shares to sell: "))
                price = float(input("Enter the selling price per share: "))
                if shares > 0 and price > 0:
                    my_portfolio.sell_stock(ticker, shares, price)
                else:
                    print("Shares and price must be positive values.")
            except ValueError:
                print("Invalid input. Please enter numbers for shares and price.")

        elif choice == '3':
            my_portfolio.view_portfolio()

        elif choice == '4':
            print("Exiting the Stock Portfolio Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()