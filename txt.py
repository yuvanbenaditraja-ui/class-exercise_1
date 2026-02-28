 BankAccount:
 class def __init__(self, account_holder, balance=0):
    self.account_holder = account_holder
    self.balance = balance
    self.transactions = []

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      self.transactions.append(f"Deposit: ${amount}")
      print(f"Deposited: ${amount}. New balance: ${self.balance}")
    else:
      print("Invalid deposit amount.")

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      self.transactions.append(f"Withdraw: {amount}")
      print(f"Withdrew: ${amount}. New balance: {self.balance}")
    else:
      print(f"Invalid withdrawal amount or insufficient balance. Current balance: {self.balance}")

  def checkbalance(self):
    print(f"Current balance: {self.balance}")

  def display_statement(self):
    print(f"\n-- Statement for {self.account_holder} --")
    if not self.transactions:
        print("No transactions yet.")
    for transaction in self.transactions:
        print(transaction)
    print(f"Current balance: {self.balance}")
    print("---------------------")

account = BankAccount("yuvan", 1000)
account.display_statement()
account.deposit(500)
account.checkbalance()
account.withdraw(200)
account.display_statement()
