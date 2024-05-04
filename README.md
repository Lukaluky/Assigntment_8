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

Overview
This Python script implements the Iterator pattern to allow users to traverse through songs in a playlist. It features a PlaylistImpl class that manages song objects and supports iteration through them using a custom iterator, SongIterator.

Features
Add Songs to Playlist: New songs can be added to the playlist with ease.
Custom Iterator Implementation: Songs in a playlist can be iterated over using a custom iterator, which supports the Python iterator protocol.
Simple Song Management: Songs are managed internally within the playlist, providing encapsulation.
How to Run
Ensure Python 3.x is installed on your machine.
Save the script to a file, for example music_player.py.
Run the script from the command line: python music_player.py.
Example Usage
The provided example in the script demonstrates:

Creating a new playlist.
Adding songs such as "Yesterday" by The Beatles, "Bohemian Rhapsody" by Queen, and "Stairway to Heaven" by Led Zeppelin.
Iterating over the songs in the playlist and printing their details.
Final Notes
These READMEs provide a brief guide to understanding and running the Python scripts. They highlight the implementation details, usage, and functionality of each pattern within the context of a practical application. This documentation is crucial for users new to design patterns or those looking for examples of Observer and Iterator implementations in Python.
