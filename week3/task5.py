def create_account(opening_balance=0.0):
    return {
        "balance": opening_balance,
        "history": [],
        "total_deposited": 0.0,
        "total_withdrawn": 0.0
    }

def check_balance(account):
    return account["balance"]

def record_transaction(account, txn_type, amount):
    transaction = {
        "type": txn_type,
        "amount": amount,
        "balance_after": account["balance"]
    }
    account["history"].append(transaction)

def deposit(account, amount):
    if amount <= 0:
        print(f"Deposit Error: Amount ({amount}) must be greater than zero.")
        return False
    
    account["balance"] += amount
    account["total_deposited"] += amount
    record_transaction(account, "deposit", amount)
    print(f"Successfully deposited: {amount:.2f}")
    return True

def withdraw(account, amount, daily_limit=2500.0, current_day_withdrawn=0.0):
    if amount <= 0:
        print(f"Withdrawal Error: Amount ({amount}) must be greater than zero.")
        return False, current_day_withdrawn
    
    if amount > account["balance"]:
        print(f"Withdrawal Error: Insufficient balance. Current balance is {account['balance']:.2f}.")
        return False, current_day_withdrawn
        
    if current_day_withdrawn + amount > daily_limit:
        remaining_limit = daily_limit - current_day_withdrawn
        print(f"Withdrawal Error: Exceeds daily limit! You can only withdraw up to {remaining_limit:.2f} more today.")
        return False, current_day_withdrawn
        
    account["balance"] -= amount
    account["total_withdrawn"] += amount
    current_day_withdrawn += amount
    record_transaction(account, "withdrawal", amount)
    print(f"Successfully withdrew: {amount:.2f}")
    return True, current_day_withdrawn

def generate_transaction_summary(account):
    print("\n" + "="*50)
    print("             BANK TRANSACTION SUMMARY             ")
    print("="*50)
    print(f"Final Balance       : {account['balance']:.2f}")
    print(f"Total Deposited     : {account['total_deposited']:.2f}")
    print(f"Total Withdrawn     : {account['total_withdrawn']:.2f}")
    print("\nTransaction History:")
    
    if not account["history"]:
        print("  No successful transactions recorded.")
    else:
        for idx, txn in enumerate(account["history"], 1):
            print(f"  {idx}. Type: {txn['type'].capitalize():<10} | Amount: {txn['amount']:<8.2f} | Balance After: {txn['balance_after']:.2f}")
    print("="*50)

def run_banking_system():
    my_account = create_account(opening_balance=2000.00)
    daily_limit = 3000.00
    today_withdrawn = 0.00

    print(f"Account opened with balance: {check_balance(my_account):.2f}\n")

    deposit(my_account, 1500.00)
    deposit(my_account, -200.00)
    
    print()
    success, today_withdrawn = withdraw(my_account, 500.00, daily_limit, today_withdrawn)
    success, today_withdrawn = withdraw(my_account, 5000.00, daily_limit, today_withdrawn)
    success, today_withdrawn = withdraw(my_account, 2800.00, daily_limit, today_withdrawn)
    success, today_withdrawn = withdraw(my_account, 1000.00, daily_limit, today_withdrawn)

    generate_transaction_summary(my_account)

if __name__ == "__main__":
    run_banking_system()