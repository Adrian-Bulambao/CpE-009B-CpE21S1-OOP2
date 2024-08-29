"""
    main.py
"""
import Accounts
import ATM

Account1 = Accounts.Accounts(serial_number = 123456,account_number =123456,account_firstname = "Royce",
                             account_lastname = "Chua",current_balance = 1000, address = "Silver Street Quezon City", email = "roycechua123@gmail.com")

serial_number1 = Account1.serial_number
print("Account 1")

print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

Account2 = Accounts.Accounts( serial_number =654321,account_number =654321,account_firstname = "John",
                             account_lastname = "Doe",current_balance = 2000,
                             address = "Gold Street Quezon City", email = "johndoe@yahoocom")


print("Account 2")
serial_number2 = Account2.serial_number
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)
print()


# Creating and Using an ATM object
ATM1 =ATM.ATM(serial_number1,500,"Deposit")
ATM1.deposit(Account1,500)
print("Account 1 Balance: ")
ATM1.check_currentbalance(Account1)
ATM1.view_transactionsummary()
print()
ATM2 =ATM.ATM(serial_number2,300,"Deposit")
ATM2.deposit(Account2, 300)
print("Account 2 Balance: ")
ATM2.check_currentbalance(Account2)
ATM2.view_transactionsummary()
