"""
A basic game of the card game built
"""

__Author__ = "Thomas Couser"

import random
from dataclasses import dataclass
from enum import Enum

class options(Enum):
    MATCH = "Match"
    ADD = "Add"
    SKIP = "Skip"


def create_deck():
    suits = ["hearts", "diamonds", "spades", "clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    cards = {}
    
    for suit in suits:
        for value in values:
            cards[f"{value} of {suit}"] = value
            background_list.append(value)
    
    return cards


def select_random_card(deck: dict):
    
    value = random.choice(list(deck.keys()))
    deck.pop(value)
    
    return f"{value}", deck


def format_message(message: str):
    print(f"***\n{message}\n***")


def deal_cards(deck: dict,location: dict, number: int):
    for i in range(number):
        card = select_random_card(deck)[0]
        deck = select_random_card(deck)[1]
        location[card] = card


def get_player_move(enum_class: Enum) -> Enum:
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
            choice = int(input(f"Enter a number between 1 and {length}: "))
            if 1 <= choice <= length:
                selected = enum_map[choice]
                return selected
            else:
                print(f"Invalid input. Enter a number between 1 and {length}")
        except:
            print("Invalid input.")


def display_location(location: dict):
    location_list = list(location.keys())
    for i in range(len(location_list)):
        print(location_list[i])


def match(player_cards: dict, table_cards: dict):
    player_cards_list = list(player_cards.keys())
    table_cards_list = list(table_cards.keys())
    matched_cards = []
    
    print(player_cards_list)
    print(table_cards_list)
    
    for e in player_cards:
            if e in table_cards:
                print(e)
                player_cards.remove(e)
                table_cards.remove(e)
    
    return player_cards, table_cards


def main():
    
    global background_list
    background_list = []
    
    starting_cards = 4
    table_cards = {}
    player_cards = {}
    
    deck = create_deck()
    
    format_message(f"The first {starting_cards} cards are: ")
    
    deal_cards(deck, table_cards, starting_cards)
    display_location(table_cards)
    
    format_message(f"Your {starting_cards} cards are: ")
    
    deal_cards(deck, player_cards, starting_cards)
    display_location(player_cards)
    
    print(background_list)
    
    # move = get_player_move(options)
    # if move == "Match":
    #     print("Match")
    #     match(player_cards, table_cards)
    # elif move == "Add":
    #     print("Add")
    # elif move == "Skip":
    #     print("Skip")
    
    
    
if __name__ == "__main__":
    main()
