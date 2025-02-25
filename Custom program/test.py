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
    
    return cards

def select_random_card(deck: dict):
    card = random.choice(list(deck.keys()))
    deck.pop(card)
    return card, deck

def format_message(message: str):
    print(f"***\n{message}\n***")

def deal_cards(deck: dict, location: dict, number: int):
    for _ in range(number):
        card, deck = select_random_card(deck)
        location[card] = card

def get_player_move(enum_class: Enum) -> Enum:
    """Displays menu and gets user's choice from an Enum class"""
    length = len(list(enum_class))
    
    enum_map = {}
    for i in range(length):
        enum_map[i + 1] = list(enum_class)[i].value
    
    print()
    
    for i in range(length):
        print(f"{i + 1}. {list(enum_class)[i].value}")
    
    print("")
    while True:
        try:
            choice = int(input(f"Enter a number between 1 and {length}: "))
            if 1 <= choice <= length:
                return enum_map[choice]
            else:
                print(f"Invalid input. Enter a number between 1 and {length}")
        except ValueError:
            print("Invalid input.")

def display_location(location: dict):
    for card in location:
        print(card)

def match(player_cards: dict, table_cards: dict):
    player_cards_list = list(player_cards.keys())
    table_cards_list = list(table_cards.keys())
    matched_cards = []
    
    for player_card in player_cards_list:
        player_value = player_cards[player_card]
        for table_card in table_cards_list:
            table_value = table_cards[table_card]
            if player_value == table_value:
                print(f"Matched {player_card} with {table_card}")
                matched_cards.append((player_card, table_card))
    
    for player_card, table_card in matched_cards:
        del player_cards[player_card]
        del table_cards[table_card]
    
    return player_cards, table_cards

def main():
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
    
    move = get_player_move(options)
    if move == "Match":
        print("Match")
        player_cards, table_cards = match(player_cards, table_cards)
        format_message("Remaining player cards:")
        display_location(player_cards)
        format_message("Remaining table cards:")
        display_location(table_cards)
    elif move == "Add":
        print("Add")
    elif move == "Skip":
        print("Skip")
    
if __name__ == "__main__":
    main()
