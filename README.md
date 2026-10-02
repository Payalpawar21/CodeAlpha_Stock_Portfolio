# Stock Portfolio Tracker

## CodeAlpha Python Programming Internship — Task 2

A simple console-based Stock Portfolio Tracker developed using Python. The program uses predefined stock prices and calculates the total investment based on the stock symbol and quantity entered by the user.

## Features

* Uses a hardcoded stock price dictionary
* Supports multiple stocks
* Accepts stock symbol and quantity from the user
* Calculates investment for each stock
* Calculates total portfolio investment
* Handles invalid stock symbols
* Allows the user to save the final result
* Saves the result in a CSV file
* Runs completely in the console

## Technologies Used

* Python
* Dictionary
* Input/Output
* Arithmetic operations
* While loop
* If-else statements
* File handling
* CSV file

## Available Stocks

The program currently uses the following sample stock prices:

| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| TSLA  |  $250 |
| GOOGL |  $150 |
| MSFT  |  $400 |
| AMZN  |  $180 |

> These are predefined sample prices used for the internship task and are not live market prices.

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run: python stock_portfolio.py
5. Enter the stock symbol.
6. Enter the quantity.
7. Enter additional stocks if required.
8. Type `done` when finished.
9. Choose `yes` if you want to save the result.

## Sample Output

Stock Portfolio Tracker
-----------------------
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity: 5

Stock price: 180
Quantity: 5
Investment: 900

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity: 2

Stock price: 250
Quantity: 2
Investment: 500

Enter stock symbol (or 'done' to finish): done

-----------------------
Total Portfolio Investment: $ 1400

Do you want to save the result? (yes/no): yes
Result saved to portfolio_result.csv


## Project Structure

Task2_Stock_Portfolio/

1.stock_portfolio.py
2.portfolio_result.csv
3.README.md


## Internship Task

This project is completed as part of the CodeAlpha Python Programming Internship.

**Task:** Task 2 — Stock Portfolio Tracker
