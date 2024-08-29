"""
    ATM.py
"""

class ATM():
    serial_number = 0
    def __init__(self, serial_number, amount, history):
        self.serial_number = serial_number
        self.amount = amount
        self.history = history
    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")

    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete")

    def check_currentbalance(self, account):
        print(account.current_balance)

    def view_transactionsummary(self):
        print(f"Transaction History: {self.history} of {self.amount}")