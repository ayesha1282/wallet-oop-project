

class DigitalWallet:
     def __init__(self, wallet_id, owner_name, opening_balance):
          self.wallet_id = wallet_id
          self.owner_name = owner_name
          self.__transaction_history = []

          if opening_balance < 0:
               print("Opening balance cannot be negative.")
               opening_balance = 0

          self.__balance = opening_balance

     def get_balance(self):
        return self.__balance

     def get_transaction_history(self):
          return list(self.__transaction_history)

     def deposit(self, amount):
          if amount <= 0:
               print("Deposit Rejected: Amount must be greater than zero")
               
          else:
               self.__balance += amount
               self.__transaction_history.append(f"Deposit: Rs. {amount}")
               print("Deposit Successful")


     def withdraw (self, amount):
          if amount <= 0:
               print("Withdrawal rejected. Amount must be greater than zero.")
          
          elif amount > self.__balance:
               print("Withdrawal rejected. Insufficient Balance.")
          else:
               self.__balance = self.__balance - amount
               self.__transaction_history.append(f"Withdrawal: Rs. {amount}")
               print("Withdrawal Successful")   

     def transfer(self, amount, receiver_wallet):
          if amount <= 0:
               print("Transfer Rejected: Amount must be greater than zero")
          elif amount > self.__balance:
               print("Transfer Rejected: Insufficient funds")
          elif receiver_wallet is self:
               print("Transfer Rejected: Cannot transfer to the same wallet")
          else:
               self.__balance -= amount
               receiver_wallet.receive_transfer(amount, self)
               self.__transaction_history.append(
                     f"Transferred Rs. {amount} to {receiver_wallet.wallet_id}")

               print("Transfer Successful")

     def receive_transfer(self, amount, sender_wallet):
        self.__balance += amount
        self.__transaction_history.append(
            f"Received Rs. {amount} from {sender_wallet.wallet_id}")

     def display_transaction_history(self):
          print(f"Transaction History of {self.wallet_id}:")
          for transaction in self.__transaction_history:
               print(transaction)

     def display_wallet(self):
        print("Wallet ID:", self.wallet_id)
        print("Owner Name:", self.owner_name)
        print("Balance: Rs.", self.get_balance())
     

wallet1 = DigitalWallet("W001", "Ayesha", 5000)
wallet2 = DigitalWallet("W002", "Ahad", 10000)
wallet3 = DigitalWallet("W003", "Abeera", 20000)
 
wallets = {
    wallet1.wallet_id: wallet1,
    wallet2.wallet_id: wallet2,
    wallet3.wallet_id: wallet3,
}

print(" ALL WALLETS ")
for wallet_id in wallets:
    wallets[wallet_id].display_wallet()
    print()
print()
print("DEPOSIT")
wallet1.deposit(2600)
wallet1.deposit(-500)

print()
print("WITHDRAWAL")
wallet1.withdraw(1000)
wallet1.withdraw(1000000)
wallet1.withdraw(-100)

print()
print("TRANSFER")
wallet1.transfer(1500, wallet2)
wallet1.transfer(1000000, wallet3)


print()
print("SEARCH WALLET")
search_id = "W002"

if search_id in wallets:
     print("Wallet found:")
     wallets[search_id].display_wallet()
else:
     print("Wallet not found.")

search_id = "W999"
if search_id in wallets:
    wallets[search_id].display_wallet()
else:
    print("Wallet W999 not found.")

print()
print("FINAL BALANCES")
for wallet_id in wallets:
    wallet = wallets[wallet_id]
    print(wallet.wallet_id, wallet.owner_name, ": Rs.", wallet.get_balance())

print()
print("TRANSACTION HISTORY")
wallet1.display_transaction_history()