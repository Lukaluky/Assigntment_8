README for the Observer Pattern: Stock Market Simulation
Overview
This Python script demonstrates the Observer pattern through a stock market simulation. The implementation includes two main classes, Stock and Investor, where Stock acts as the subject and Investor as the observer. The program allows dynamic registration and deregistration of investors to stocks, and notifies them of price changes automatically.

Features
Dynamic Investor Registration: Investors can be registered to any stock to receive updates on price changes.
Price Update Notification: Any change in stock prices notifies all registered investors of the new price.
Dynamic Investor Deregistration: Investors can be removed from a stock's notification list at any time.
How to Run
Ensure Python 3.x is installed on your machine.
Save the script to a file, for example stock_market.py.
Run the script from the command line: python stock_market.py.
Example Usage
The provided example in the script demonstrates:

Creating stock objects for "AAPL" and "GOOG".
Creating investor objects "John Doe" and "Jane Doe".
Registering investors to stocks and updating stock prices.
Notifying investors of price updates and unregistering an investor.
