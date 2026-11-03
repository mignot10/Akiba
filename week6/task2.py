class BankAccount:
    def __init__(self, account_holder, init_balance = 0):
        self.account_holder = account_holder
        self.__balance = init_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.__balance:.2f}")


    def get_balance(self):
        return self.__balance

account1 = BankAccount("Egelit Egele", 5000.0)
print(f"Account Holder: {account1.account_holder}")
print(f"Initial Balance: ${account1.get_balance()}")

account1.deposit(50.0)
account1.withdraw(30.0)
account1.withdraw(200.0)