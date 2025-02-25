"""Simple banking program"""  

__Author__ = "Thomas Couser"

import random
from enum import Enum
from banking_functions import get_float, get_integer, get_enum_choice
import json

list_of_accounts = []

class Bank:
    """Bank class"""
    
    def __init__(self):
        self.accounts = {}
        self.transactions = {}
    
    
    def create_account(self):
        """Create a new bank account"""
        
        account_name = input("Enter account name: ")
        start_balance = get_float("Enter starting balance: ")
        account_number = generate_account_number(8)
        account = BankAccount(account_name, start_balance, account_number)
        self.accounts[account_number] = account
        self.transactions[account_number] = []
        print(f"Account created. Account number: {account_number}")
        list_of_accounts.append(account)
        return account
    
    
    def get_account(self, account_number):
        """Get a bank account based on account number"""
        account = self.accounts.get(account_number)
        return account
    
    
    def transaction(self):
        """Perform a transaction"""
        account_number = get_integer("Enter account number: ")
        account = self.get_account(account_number)
        if not account:
            print("Account not found.")
            return "Account not found."
        
        
        transaction_type = get_enum_choice(TransactionType)
        match transaction_type:
            case "Deposit":
                amount = get_float("Enter amount to deposit: ")
                account.deposit(amount)
            case "Withdraw":
                amount = get_float("Enter amount to withdraw: ")
                account.withdraw(amount)
            case "Cancel":
                print("Transaction cancelled.")
                return "Transaction cancelled."
        
        
        self.transactions[account_number].append((transaction_type, amount))
        print("Transaction completed.")
        return "Transaction completed."
    
    
    def get_transaction_history(self, account_number):
        """Get transaction history"""
        transactions = self.transactions.get(account_number, [])
        return transactions
    
    
    def check_balance(self):
        """Check balance"""
        account_number = get_integer("Enter account number: ")
        account = self.get_account(account_number)
        if not account:
            return "Account not found."
        
        balance = account.get_balance()
        print(f"Balance: ${balance}")
        return f"Balance: ${balance}"
    
    def view_all_accounts(self):
        """View all bank accounts"""
        
        for account in self.accounts.values():
            print(account)
    
    
    def show_transactions(self, account_number: int):
        """Show transaction history"""
        transactions = self.get_transaction_history(account_number)
        if transactions:
            print("Transaction history:\n")
            for trans, amount in transactions:
                print(f"{trans}: ${amount}")
        else:
            print("No transactions found.")


class BankAccount:
    """Bank account class"""

    def __init__(self,name: str,balance: float, account_number):
        
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    
    def deposit(self, amount: float):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
    
    
    def withdraw(self, amount: float):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
    
    
    def get_balance(self):
        """Get the balance of the account"""
        balance = self.balance
        return balance
    
    
    def __str__(self):
        return f"\nAccount name: {self.name}"


def save(path: str):
    """Save bank accounts to a txt file"""
    with open(path, 'w') as f:
        f.write("Bank accounts:\n\n")
        for account in list_of_accounts:
            f.write(f"Account name: {account.name}\nAccount number: {account.account_number}\n\n")
    print(f"Accounts saved to {path}.")


def save_json():
    """Save bank accounts to a JSON file"""
    with open('accounts.json','w') as f:
        json.dump(list_of_accounts, f)


class MenuOptions(Enum):
    """Enumeration for menu options"""
    CREATE_ACCOUNT = "Create account"
    PERFORM_TRANSACTION = "Perform transaction"
    CHECK_BALANCE = "Check balance"
    TRANSACTION_HISTORY = "Transaction history"
    VIEW_ALL_ACCOUNTS = "View all accounts"
    SAVE = "Save"
    EXIT = "Exit"


class TransactionType(Enum):
    """Enumeration for transaction types"""
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    CANCEL = "Cancel"


def generate_account_number(digits: int) -> int:
    #code = random.randint(10000000, 99999999)
    lower = 10 ** (digits - 1)
    upper = 10 ** (digits) - 1
    
    code = random.randint(lower, upper)
    return code


def main():
    bank = Bank()
    PATH = "/Users/thomascouser/Downloads/Bank Accounts.txt" #For Mac
    #PATH = "C:/Users/University/Downloads/Bank Accounts.txt" #For Windows
    
    choice: int = 0
    
    print("Welcome to the banking program")
    
    while choice != "Exit":
        choice = get_enum_choice(MenuOptions)
        
        match choice:
            case "Create account":
                print("Create account")
                bank.create_account()
                
            case "Perform transaction":
                print("Perform transaction")
                bank.transaction()
                
            case "Check balance":
                print("Check balance")
                bank.check_balance()
            
            case "View all accounts":
                print("Displaying accounts")
                bank.view_all_accounts()
                
            case "Transaction history":
                account_number = get_integer("Enter account number: ")
                bank.show_transactions(account_number)
            
            case "Save":
                save(PATH)
                #save_json()
                
            case "Exit":
                print("Goodbye!")

if __name__ == "__main__":
    main()
