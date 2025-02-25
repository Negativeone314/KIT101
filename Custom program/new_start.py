from enum import Enum, auto

class ExpenseCategory(Enum):
    FOOD = auto()
    TRANSPORTATION = auto()
    UTILITIES = auto()
    ENTERTAINMENT = auto()
    OTHER = auto()

class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        if isinstance(expense, Expense):
            self.expenses.append(expense)
        else:
            raise ValueError("Invalid expense")

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def expenses_by_category(self):
        category_totals = {category: 0 for category in ExpenseCategory}
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount
        return category_totals

def print_expenses_by_category(expenses_by_category):
    for category, total in expenses_by_category.items():
        print(f"{category.name.capitalize()}: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter description of the expense: ")
            amount = float(input("Enter amount of the expense: "))
            print("Expense Categories:")
            for i, category in enumerate(ExpenseCategory, start=1):
                print(f"{i}. {category.name.capitalize()}")
            category_index = int(input("Enter the category number: ")) - 1
            category = list(ExpenseCategory)[category_index]
            expense = Expense(description, amount, category)
            tracker.add_expense(expense)
            print("Expense added successfully!")
        
        elif choice == "2":
            total_expenses = tracker.total_expenses()
            print(f"Total Expenses: ${total_expenses:.2f}")
        
        elif choice == "3":
            expenses_by_category = tracker.expenses_by_category()
            print_expenses_by_category(expenses_by_category)
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
