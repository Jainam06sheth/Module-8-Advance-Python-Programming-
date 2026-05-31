'''Write a Python program to demonstrate the use of local and global variables in a class.'''

# Global variable :
bank_name = "ABC National Bank"

class BankAccount:
    
    def create_account(self, name, balance):
        # Local variables :
        account_holder = name
        initial_balance = balance

        print("Bank Name:", bank_name)  # global variable
        print("Account Holder:", account_holder)  # local variable
        print("Initial Balance:", initial_balance)  # local variable

    def show_bank(self):
        print("\nWelcome to", bank_name)  # global variable again used


acc = BankAccount()

acc.create_account("Dhruvi Mandloi", 5000)
acc.show_bank()