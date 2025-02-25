"""Functions for the banking program"""

__Author__ = "Thomas Couser"

from enum import Enum

def get_float(prompt: str) -> float:
    """Get a float from the user"""
    num = None
    while num is None:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except:
            num = None
            print("Please enter a number")


def get_integer(prompt: str) -> int:
    """Get an integer from the user"""
    num = None
    while num is None:
        num = input(prompt)
        try:
            num = int(num)
            return num
        except:
            num = None
            print("Please enter an integer")


def get_enum_choice(enum_class: Enum) -> str:
    """Displays menu and gets user's choice from an Enum class"""
    
    length = len(list(enum_class))
    
    enum_map = {}
    for i in range(0, length):
        enum_map[i+1] = list(enum_class)[i].value
    
    print()
    
    for i in range(length):
        print(f"{i+1}. {list(enum_class)[i].value}")
    
    print("")
    while True:
        try:
            choice = get_integer(f"Enter your choice between 1 and {length}: ")
            if 1 <= choice <= len(enum_class):
                selected = enum_map[choice]
                return selected
            else:
                print(f"Invalid input. Enter a number between 1 and {length}")
        except:
            print("Invalid input.")