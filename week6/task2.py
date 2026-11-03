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


# ==============================================================================
# ANSWERS
# ==============================================================================

# 1. What is encapsulation?
# Encapsulation is an OOP principle that binds data (attributes) and methods together 
# inside a class, while restricting direct outside access to internal state to prevent 
# unintended modifications.

# 2. Why do we use private attributes?
# Private attributes protect sensitive data from being altered directly from outside 
# the class, forcing data modification to go through controlled methods (like getters 
# and setters) where validation logic can be applied.

# 3. What is name mangling in Python?
# Name mangling is Python's internal mechanism for attributes prefixed with double 
# underscores (e.g., __balance). Python automatically transforms the attribute name to 
# _ClassName__attribute (e.g., _BankAccount__balance) to prevent accidental external 
# access or overriding in subclasses.

# 4. What is the difference between public, protected, and private naming conventions?
# - Public (e.g., self.name): Accessible from anywhere, inside or outside the class.
# - Protected (e.g., self._balance): Prefixed with a single underscore; signals to developers 
#   that it should only be accessed inside the class and its subclasses (convention only).
# - Private (e.g., self.__balance): Prefixed with double underscores; triggers name mangling 
#   to strictly block direct access outside the class.
