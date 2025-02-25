"""
KIT101 5.4DN Text Map

Command-driven program for working with grid-based maps rendered as text.
"""

import numpy as np
import math

__Author__ = "Thomas Couser"


def create_map(string: str) -> np.ndarray:
    """
    Converts the multi-line string into a 2D array of single-letter strs.
    Each line in the str should be the same length for best results.
    """
    rows = string.splitlines()
    map = np.empty((len(rows), len(rows[0])), dtype=str)
    
    if len(rows) > 0:
        for i, line in enumerate(rows):
            map[i] = list(line)
            
    return map


def display_bordered_title(title: str):
    """
    Presents the given title text with a border of equals signs.
    """
    BORDER = "=" * (len(title) + 4)
    print(BORDER)
    print(f"= {title} =")
    print(BORDER)
    print()


def display_help():
    """
    Displays a list of available program commands.
    """
    print("Commands:\n"
          "?                \tShow this list of commands\n"
          "d                \tDisplay the map\n"
          "z row col        \tShow grid squares surrounding (row, col) \n"
          "r row col colour \tReplace region with colour (a single character) starting ar (row, col) \n"
          "l filename       \tLoad the text map from filename \n"
          "s filename       \tSave the current map to filename \n"
          "q                \tExit the program \n"
          "\nCommands may be chained together, separated by whitespace."
        "\nNote that coordinates behave in an x,y order and the top left corner is 1,1.")


def display_map(map: np.array):
    """
    Displays the given character-based map with a leading and trailing blank line.
    """
    print()
    for row in map:
        for i in row:
            print(f"{i} ", end="")
        print()
    print()


def is_inside(map: np.ndarray, row: int, col: int) -> bool:
    """
    Returns True if (row, col) is inside the map's bounds; False otherwise.
    """
    num_rows, num_cols = map.shape
    if 0 < row < num_rows+1 and 0 < col < num_cols+1:
        return True
    else:
        return False


def zoom(map: np.array, row, col):
    """
    Displays the 9 grid squares in the map centred at (row, col).
    Displays a space for any grid square that are outside the map's bounds.
    """
    
    zoomed = np.empty(shape=9,dtype=str)
    index = 0
    q = 2
    while q >= 0:
        n = 2
        while n >= 0:
            position = row-q,col-n
            if is_inside(map,row-q+1,col-n+1) == False:
                #print("no")
                zoomed[index] = ""
            else:
                element = map[position]
                #print("yes")
                zoomed[index] = element
            n += -1
            index += 1
        q += -1
    zoomed.shape = (3,3)
    display_map(zoomed)


def replace(map: np.ndarray, row: int, col: int, new_colour: str) -> int:
    """
    Starts a flood fill operation by selecting the replacement grid square
    value at the given row and col. Returns the number of cells modified.
    """
    if row > map.shape[0]-1 or col > map.shape[1]-1:
        print("")
        print("Error: out of bounds")
    else:
        current_colour = map[row,col]
        
    list_of_changes = []
    
    def fill(row,col):
        
        if row == map.shape[0] or col == map.shape[1]:
            ...
        else:
            if 0<=row<= map.shape[0] and 0<=col<= map.shape[1] and map[row,col] == current_colour and map[row,col] != new_colour:
                
                map[row,col] = new_colour
                list_of_changes.append(new_colour)
                #print("test")
                fill(row+1,col)
                fill(row-1,col)
                fill(row,col+1)
                fill(row,col-1)
            
    fill(row,col)
    display_map(map)
    changed = len(list_of_changes)
    print(f"Number of cells changed: {changed}")
    return changed

def main():
    
    map: np.ndarray # The character-based map
    command: list # User's entered command and parameters
    row: int # Command param for row
    col: int # Command param for col
    colour: str # Command param for colour
    
    display_bordered_title("Text Map")
    
    str_map = ("a b c d e f \n"
               "g h h h h l \n"
               "m h h h q r \n"
               "s h h h w x \n"
               "y z h b c d \n"
               "e f g h i j").split()
    
    map = np.array(str_map)
    map.shape = (int(math.sqrt(len(map))),int(math.sqrt(len(map))))
    
    command = input("Enter commands (? for help). "
                    "There are no further prompts after this point.\n").split()
    
    
    while command != ["q"]:
        match command:
            # TODO: Make required changes in the appropiate cases
            case ["d"]: # Display
                display_map(map)
            case ["z", row, col]: # Zoom
                row = int(command[1])
                col = int(command[2])
                zoom(map,row,col)
            case ["r", row, col, new_colour]: # Replace
                replace(map, int(command[2])-1, int(command[1])-1, command[3])
            case ["l"]: # Load
                print("Feature not implemented")
            case ["s"]: # Save
                print("Feature not implemented")
            case ["q"]: # Quit
                break
            case _:   # Unknown command. Will also capture ?
                display_help()
                
        command = input().split()
    print("Exiting...")
if __name__ == "__main__":
    main()
