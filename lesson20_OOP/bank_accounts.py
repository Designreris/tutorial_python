# BANK ACCOUNTS

class BalanceException(Exception):
  pass


class BankAccount:
  def __init__(self, initial_amount, account_name):
    self.balance  = initial_amount
    self.name = account_name
    print(f"\nAccount '{self.name}' created.\nBalance  =  ${self.balance:.2f}")
  
  def get_balance(self):
    print(f"Account '{self.name}' Balance = ${self.balance:.2f}")
  
  def deposit(self, amount):
    self.balance = self.balance + amount
    print("Deposit complete.")
    self.get_balance()

  def viable_transaction(self, amount):
    if self.balance >= amount:
      return
    else:
      raise BalanceException(
        f"\nSorry, account '{self.name}' has insufficient funds!\nBalance: '${self.balance:.2f}'."
      )
  
  def withdraw(self, amount):
    try:
      self.viable_transaction(amount)
      self.balance =  self.balance - amount
      print('Withdraw complete.')
      self.get_balance()
    except BalanceException as error:
      print(f"\nWithdraw interrupted: {error}")

  def transfer(self, amount, account_name):
    try:
      print('\n***************\n\nBeginning Transfer...')
      self.viable_transaction(amount)
      self.withdraw(amount)
      account_name.deposit(amount)
      print('Transfer complete!\n\n***************')
    except BalanceException as error:
      print(f"\nTransfer interrupted: {error}")

class InterestRewardsAccount(BankAccount):
  def deposit(self, amount):
    self.balance = self.balance + (amount * 1.05)
    print("Deposit complete.")
    self.get_balance()

class SavingsAccount(InterestRewardsAccount):
  def __init__(self, initial_amount, account_name):
    super().__init__(initial_amount, account_name)
    self.fee = 5

  def withdraw(self, amount):
    try:
      self.viable_transaction(amount + self.fee)
      self.balance = self.balance - (amount + self.fee)
      print("Withdraw completed.")
      self.get_balance()
    except BalanceException as error:
      print(f"Withdraw interrupted: {error}")
