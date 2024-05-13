'''
Write a python program to replicate a Banking system. The following features are mandatory:
1. Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also.
'''
class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs.{amount} successful. Your new balance is Rs.{self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs.{amount} successful. Your new balance is Rs.{self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Your current balance is Rs.{self.balance}.")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully.")

def login(accounts):
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if account_number in accounts and accounts[account_number].pin == pin:
        return accounts[account_number]
    else:
        print("Invalid account number or PIN.")
        return None

def main():
    accounts = {
        "123456": BankAccount("123456", "1234", 1000),
        "789012": BankAccount("789012", "5678", 500)
    }  # Example accounts

    while True:
        print("\n1. Login")
        print("2. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            user_account = login(accounts)
            if user_account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Change PIN")
                    print("5. Logout")
                    option = input("Please select an option: ")

                    if option == "1":
                        amount = float(input("Enter the amount to deposit: Rs."))
                        user_account.deposit(amount)
                    elif option == "2":
                        amount = float(input("Enter the amount to withdraw: Rs."))
                        user_account.withdraw(amount)
                    elif option == "3":
                        user_account.display_balance()
                    elif option == "4":
                        new_pin = input("Enter your new PIN: ")
                        user_account.change_pin(new_pin)
                    elif option == "5":
                        print("Logged out.Thank You")
                        break
                    else:
                        print("Invalid option.")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occured", e)

'''
OUTPUT
------
"E:\entri\DSML projects\venv\Scripts\python.exe" "E:/entri/DSML projects/basics/banking system FA2.py"

1. Login
2. Exit
Please select an option: 1
Enter your account number: 123456
Enter your PIN: 12
Invalid account number or PIN.

1. Login
2. Exit
Please select an option: 1
Enter your account number: 123456
Enter your PIN: 1234

1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Logout
Please select an option: 3
Your current balance is Rs.1000.

1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Logout
Please select an option: 1
Enter the amount to deposit: Rs.2000
Deposit of Rs.2000.0 successful. Your new balance is Rs.3000.0.

1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Logout
Please select an option: 2
Enter the amount to withdraw: Rs.1000
Withdrawal of Rs.1000.0 successful. Your new balance is Rs.2000.0.

1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Logout
Please select an option: 3
Your current balance is Rs.2000.0.

1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Logout
Please select an option: 4
Enter your new PIN: 1213
PIN changed successfully.

1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Logout
Please select an option: 5
Logged out.Thank You

1. Login
2. Exit
Please select an option: 2
Exiting...

Process finished with exit code 0

'''
