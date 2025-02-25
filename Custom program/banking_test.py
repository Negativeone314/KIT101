"""
Simple banking program
"""

__Author__ = "Thomas Couser"

import banking_functions as fn

def main():
    choice: int = 0
    
    print("Welcome to the banking program")
    
    while choice != "Exit":
        choice = fn.get_enum_choice(fn.MenuOptions)
        
        match choice:
            case "Create account":
                print("Create account")
                fn.add_account()
            
            case "Perform transaction":
                print("Perform transaction")
            
            case "Check balance":
                print("Check balance")
                
            
            case "Transaction history":
                print("Transaction history")
            
            case "Exit":
                print("Goodbye!")


if __name__ == "__main__":
    main()