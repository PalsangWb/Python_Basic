# Base Class: Account
class Account:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []  

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount: Amount should be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited amount: ${amount}")
        return f"Deposited amount: ${amount} and Current balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdraw amount: Amount should be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrawn amount: ${amount}")
        return f"Withdrawn amount: ${amount} and Current balance: ${self.balance}"

    def view_balance(self):
        return f"Current balance: ${self.balance}"

    def view_transactions(self):
        if not self.transactions:
            return "There are no transactions yet."
        return "\n".join(self.transactions)


# Subclass: CheckingAccount
class CheckingAccount(Account):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdraw amount: Amount should be positive")
        if amount > self.balance + 100:  # Overdraft limit set to $100
            raise ValueError(f"Cannot withdraw more than your balance + $100 overdraft limit.")
        self.balance -= amount
        self.transactions.append(f"Withdrawn (Overdraft allowed): ${amount}")
        return f"Withdrawn amount: ${amount} and Current balance: ${self.balance}"

    def transfer(self, amount, transfer_account):
        if amount <= 0:
            raise ValueError("Invalid transfer amount: Amount should be positive")
        if amount > self.balance:
            raise ValueError("Insufficient amount for transfer.")
        self.balance -= amount
        transfer_account.deposit(amount)
        self.transactions.append(f"Transferred amount: ${amount} to {transfer_account.account_holder}")
        return f"Transferred amount: ${amount} to {transfer_account.account_holder} and Current balance: ${self.balance}"


# Subclass: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.1):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate  # Annual interest rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added: ${interest}")
        return f"Interest added: ${interest}. Current balance: ${self.balance}"


# Main function: User interaction
def main():
    print("Welcome to our bank account.")
    try:
        account_type = input("Would you like to create a Checking or Savings account? (C/S): ").strip().lower()

        account_holder = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        # Create the account based on the type selected
        if account_type == "c":
            account = CheckingAccount(account_holder, initial_balance)
        elif account_type == "s":
            interest_rate = float(input("Enter interest rate: "))
            account = SavingsAccount(account_holder, initial_balance, interest_rate)
        else:
            raise ValueError("Invalid account type. Please choose 'C' for Checking or 'S' for Savings.")

        while True:
            if isinstance(account, SavingsAccount):
                print("\nOptions: 1. Deposit 2. Withdraw 3. Transfer 4. Add Interest 5. View Balance 6. View Transactions 7. Exit")
            else:
                print("\nOptions: 1. Deposit 2. Withdraw 3. Transfer 4. View Balance 5. View Transactions 6. Exit")
                
            choose = input("Enter your option: ").strip()

            if choose == "1":
                amount = float(input("Enter amount to deposit: "))
                print(account.deposit(amount))
            elif choose == "2":
                amount = float(input("Enter amount to withdraw: "))
                print(account.withdraw(amount))
            elif choose == "3":
                transfer_account_holder = input("Enter the transfer account holder's name: ")
                transfer_account_balance = float(input("Enter the transfer account's initial balance: "))
                transfer_account = CheckingAccount(transfer_account_holder, transfer_account_balance)
                amount = float(input("Enter amount to transfer: "))
                print(account.transfer(amount, transfer_account))
            elif choose == "4" and isinstance(account, SavingsAccount):
                print(account.add_interest())
            elif choose == "5":
                print(account.view_balance())
            elif choose == "6":
                print("\nTransaction History:")
                print(account.view_transactions())
            elif choose == "7":
                print("Thank you for using our bank account.")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
