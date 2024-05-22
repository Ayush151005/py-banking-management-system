class Bank:
    def __init__(self):
        self.accounts = {}
        self.statements = []

    def open_account(self):
        print("\nPlease provide some information")
        name = input("Enter Your Name: ")
        account_no = input("Choose Account No: ")
        password = input("Create Password: ")
        balance = float(input("Deposit Account opening balance: "))
        self.accounts[account_no] = {'name': name, 'password': password, 'balance': balance}
        print("\nYour Account is Opened successfully\n")

    def check_balance(self):
        user_acc_no = input("Enter Your Account No: ")
        user_password = input("Enter Your Password: ")
        account = self.accounts.get(user_acc_no)
        if account and account['password'] == user_password:
            print("\nYour Balance is", account['balance'], "Rupees\n")
        else:
            print("\nBalance check Process failed due to incorrect information. Please try again\n")

    def deposit_money(self):
        user_acc_no = input("Enter Your Account No: ")
        user_password = input("Enter Your Password: ")
        account = self.accounts.get(user_acc_no)
        if account and account['password'] == user_password:
            deposit_amount = float(input("Enter Deposit Amount: "))
            account['balance'] += deposit_amount
            print("\n", deposit_amount, "Rupees is deposited successfully\n")
        else:
            print("\nDeposit Process failed due to incorrect information. Please try again\n")

    def withdraw_money(self):
        user_acc_no = input("Enter Your Account No: ")
        user_password = input("Enter Your Password: ")
        account = self.accounts.get(user_acc_no)
        if account and account['password'] == user_password:
            withdraw_amount = float(input("Enter Withdrawable Amount: "))
            if account['balance'] < withdraw_amount:
                print("\nSorry! You don't have enough Money to withdraw\n")
            else:
                account['balance'] -= withdraw_amount
                print("\n", withdraw_amount, "Rupees is withdrawal successfully\n")
        else:
            print("\nWithdraw Process failed due to incorrect information. Please try again\n")

    def transfer_money(self):
        sender_acc_no = input("Enter Your Account No: ")
        sender_password = input("Enter Your Password: ")
        sender_account = self.accounts.get(sender_acc_no)
        if sender_account and sender_account['password'] == sender_password:
            receiver_acc_no = input("Enter receiver's Account No: ")
            receiver_account = self.accounts.get(receiver_acc_no)
            if receiver_account:
                transfer_amount = float(input("Enter Transfer Amount: "))
                if sender_account['balance'] < transfer_amount:
                    print("\nSorry! You don't have enough Money to Transfer\n")
                else:
                    sender_account['balance'] -= transfer_amount
                    receiver_account['balance'] += transfer_amount
                    print("\n", transfer_amount, "Rupees is transferred successfully\n")
            else:
                print("\nReceiver's Account not found. Transfer Process failed\n")
        else:
            print("\nTransfer Process failed due to incorrect information. Please try again\n")

    def show_statement(self):
        user_acc_no = input("Enter Your Account No: ")
        user_password = input("Enter Your Password: ")
        account = self.accounts.get(user_acc_no)
        if account and account['password'] == user_password:
            print("\n  Name   \tAccount No  \tBalance\n")
            print(account['name'], "\t", user_acc_no, "\t", account['balance'])
        else:
            print("\nStatement check failed due to incorrect information. Please try again\n")


def main():
    bank = Bank()
    print("\nBANKING MANAGEMENT SYSTEM\n")
    while True:
        print("Press 1 to Open Account")
        print("Press 2 to Check Balance")
        print("Press 3 to Deposit Money")
        print("Press 4 to Withdraw Money")
        print("Press 5 to Transfer Money")
        print("Press 6 to Show Statement")
        print("Press 7 to Exit")
        choice = input("Choose your choice: ")
        if choice == '1':
            bank.open_account()
        elif choice == '2':
            bank.check_balance()
        elif choice == '3':
            bank.deposit_money()
        elif choice == '4':
            bank.withdraw_money()
        elif choice == '5':
            bank.transfer_money()
        elif choice == '6':
            bank.show_statement()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again\n")


if __name__ == "__main__":
    main()
