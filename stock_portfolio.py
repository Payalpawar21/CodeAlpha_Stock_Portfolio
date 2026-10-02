stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

print("Stock Portfolio Tracker")
print("-----------------------")

total_investment = 0

while True:
    stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock symbol not found.")
        print()
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity

    total_investment += investment

    print("Stock price:", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Investment:", investment)
    print()

print("-----------------------")
print("Total Portfolio Investment: $", total_investment)

save_result = input("Do you want to save the result? (yes/no): ").lower()

if save_result == "yes":
    with open("portfolio_result.csv", "w") as file:
        file.write("Total Portfolio Investment\n")
        file.write(str(total_investment))

    print("Result saved to portfolio_result.csv")