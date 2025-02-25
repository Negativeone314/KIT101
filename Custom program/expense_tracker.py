"""
Project: Expense Tracker
"""

__Author__ = "Thomas Couser"

from enum import Enum
from dataclasses import dataclass


class StartOptions(Enum):
    """Enumeration for start options"""
    ADD_ACCOUNT = 1
    ENTER_ACCOUNT = 2
    VIEW_ACCOUNTS = 3
    QUIT = 4

class MenuOptions(Enum):
    """Enumeration for menu options"""
    ADD_EXPENSE = 1
    EDIT_EXPENSE = 2
    DELETE_EXPENSE = 3
    VIEW_EXPENSES = 4
    SHOW_MOST_EXPENSIVE = 5
    SHOW_AVERAGE_EXPENSE = 6
    QUIT = 7


class Categories(Enum):
    """Enumeration for expense categories"""
    FOOD = "Food"
    TRANSPORTATION = "Transportation"
    HOUSING = "Housing"
    UTILITIES = "Utilities"
    ENTERTAINMENT = "Entertainment"
    OTHER = "Other"


@dataclass
class Expense:
    """Dataclass to represent each expense"""
    amount: int # amount of the expense
    category: Categories # category of the expense
    
    def __str__(self) -> str:
        return f"{self.category}: {self.amount} spent on {self.description}"
    
    def __init__(self, description: str, amount: int, category: Categories):
        self.description = description
        self.amount = amount
        self.category = category


def check_account(dict: dict, id: str) -> bool:
    """Checks if an account exists"""

def get_integer(prompt: str, min_value: int = None, max_value: int = None) -> int:
    """
    Get an integer from the user.
    """
    
    num: int = None
    
    while num is None:
        num = input(prompt)
        try:
            num = int(num)
            if min_value <= num <= max_value:
                return num
            else:
                num = None
                print(f"Number must be between {min_value} and {max_value}")
        except:
            num = None
            print(f"Please enter an integer")


def get_enum_choice(enum_class: Enum) -> Enum:
    """Displays menu and gets user's choice from an Enum class"""
    
    length = len(list(enum_class))
    
    enum_map = {}
    for i in range(0, length):
        enum_map[i+1] = list(enum_class)[i].value
    
    print("Choose one of the following: ")
    
    for i in range(length):
        print(f"{i+1}. {list(enum_class)[i].value}")
    
    print("")
    while True:
        try:
            choice = get_integer(f"Enter your choice between 1 and {length}: ",1,length)
            if 1 <= choice <= len(enum_class):
                selected = enum_map[choice]
                return selected
            else:
                print(f"Invalid input. Enter a number between 1 and {length}")
        except:
            print("Invalid input.")


def create_expense() -> Expense:
    expense = 0
    
    print()
    
    description = input("Enter description: ")
    amount = get_integer("Enter amount: ",0,1000)
    category = get_enum_choice(Categories)
    
    expense = Expense(description, amount, category)
    
    return expense


def add_expense(list: list) -> None:
    expense: Expense
    expense = create_expense()
    list.append(expense)
    print(f"Expense added: {expense}\n")


def most_expensive(list: list) -> Expense:
    
    most_expensive = None
    
    for expense in list:
        if most_expensive is None or expense.amount > most_expensive.amount:
            most_expensive = expense
    
    return most_expensive


def calculate_average(list: list) -> float:
    total = 0
    for expense in list:
        total += expense.amount
    
    return total / len(list)


def edit_expense():
    print("Edit expense\n")
    


def delete_expense(list: list) -> None:
    print("Delete expense\n")
    did = 0
    description = input("Enter description: ")
    
    for expense in list:
        if expense.description == description:
            list.remove(expense)
            did = 1
            print(f"\nExpense deleted: {expense}\n")
            break
    
    if did == 0:
        print("\nExpense not found\n")


def view_expenses(list: list) -> None:
    print(f"List of {len(list)} expenses: \n")
    
    for expense in list:
        print(expense)
    
    print()


def main():
    choice: int = 0
    list_of_expenses: list[Expense] = []
    num_options = len(list(MenuOptions))
    accounts = {}
    
    list_of_expenses.append(Expense("Donut", 50, "Food"))
    list_of_expenses.append(Expense("Car", 100, "Transportation"))
    
    while choice != MenuOptions.QUIT:
        print("Expense Tracker")
        for option in MenuOptions:
            print(f"{option.value}. {option.name.capitalize().replace('_', ' ')}")
        choice = get_integer("Enter your choice: ", 1, num_options)
        option = MenuOptions(choice) if choice in MenuOptions else None
        
        # match option:
        #     case MenuOptions.ADD_EXPENSE:
        #         add_expense(list_of_expenses)
        #     case MenuOptions.EDIT_EXPENSE:
        #         edit_expense(list_of_expenses)
        #     case MenuOptions.DELETE_EXPENSE:
        #         delete_expense(list_of_expenses)
        #     case MenuOptions.VIEW_EXPENSES:
        #         view_expenses(list_of_expenses)
        #     case MenuOptions.SHOW_MOST_EXPENSIVE:
        #         print(f"\nMost expensive expense: {most_expensive(list_of_expenses)}\n")
        #     case MenuOptions.SHOW_AVERAGE_EXPENSE:
        #         print(f"\nAverage expense: {calculate_average(list_of_expenses)}\n")
        #     case MenuOptions.QUIT:
        #         print("Exiting...")
        #     case _:
        #         print("Invalid option")


if __name__ == "__main__":
    main()
