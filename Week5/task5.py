# ==========================
# Task 5: Bank Account Management
# ==========================

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"{amount} Birr deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"{amount} Birr withdrawn successfully.")

    def display_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: {self.balance} Birr")


# Create two bank account objects
account1 = BankAccount("Abebe", 1000)
account2 = BankAccount("Hana", 3000)

# Perform transactions on account 1
print("=== Account 1 ===")
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)
account1.display_balance()

print()

# Perform transactions on account 2
print("=== Account 2 ===")
account2.deposit(1000)
account2.withdraw(500)
account2.withdraw(4000)
account2.display_balance()
