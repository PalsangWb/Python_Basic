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
            # Print the available options
            if isinstance(account, SavingsAccount):
                print("\nOptions: 1. Deposit 2. Withdraw 3. Transfer 4. Add Interest 5. View Balance 6. View Transactions 7. Exit")
            else:
                print("\nOptions: 1. Deposit 2. Withdraw 3. Transfer 4. View Balance 5. View Transactions 6. Exit")
                
            choose = input("Enter your option: ").strip()  # Use .strip() to remove any extra spaces or characters

            print(f"User chose option: {choose}")  # Debugging line to confirm the user's choice

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
            elif choose == "4":
                print(account.view_balance())  # View balance
            elif choose == "5":
                print(account.view_transactions())  # View transactions
            elif choose == "6":
                print("Thank you for using our bank account.")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
