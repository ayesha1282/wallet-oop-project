# Secure Digital Wallet (Python, OOP)

A digital wallet program built with Object-Oriented Programming in Python.
Created for Introduction to Object Oriented Programming, BS Financial Technology, Government College University, Lahore.

## Features
- `DigitalWallet` class with wallet ID, owner name, balance and transaction history
- Deposit, withdraw and transfer between wallets
- Validation: rejects zero or negative amounts, insufficient balance and transfers to the same wallet
- Wallets stored in a dictionary, so any wallet can be searched by ID
- Transaction history for each wallet

## OOP concepts used
- **Encapsulation:** balance and transaction history are private (`__balance`, `__transaction_history`) and change only through class methods. `get_transaction_history()` returns a copy of the list.
- **Abstraction:** users work through simple public methods such as `deposit()`, `withdraw()`, `transfer()` and `display_wallet()`.


Author: Ayesha Mudassar
