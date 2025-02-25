"""
KIT101 5.4DN Text Map

Command-driven program for working with grid-based maps rendered as text.
"""

import numpy as np

__author__ = "Thomas Couser"


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
          "\nCommands may be chained together, separated by whitespace.")


def display_map(map: np.array):
    """
    Displays the given character-based map with a leading and trailing blank line.
    """
    print()
    for row in map:
        for i in row:
            print(i,end="")
        print()
    print()


def is_inside(map: np.ndarray, row: int, col: int) -> bool:
    """
    Returns True if (row, col) is inside the map's bounds; False otherwise.
    """
    # TODO: Implement this
    num_rows, num_cols = map.shape
    if 0 < row < num_rows and 0 < col < num_cols:
        return True
    else:
        return False


def zoom(map: np.ndarray, row: int, col: int):
    """
    Displays the 9 grid squares in the map centred at (row, col).
    Displays a space for any grid square that are outside the map's bounds.
    """
    # TODO: Implement this (replace the elipses ... below)
    zoomed = f"{map[row-1, col-1]}{map[row-1, col]}{map[row-1, col+1]}\n" \
             f"{map[row, col-1]}{map[row, col]}\\{map[row, col+1]}\n" \
             f"{map[row+1, col-1]}{map[row+1, col]}{map[row+1, col+1]}"
    zoomed_map = create_map(zoomed)
    display_map(zoomed_map)


def replace(map: np.ndarray, row: int, col: int, with_colour: str) -> int:
    """
    Starts a flood fill operation by selecting the replacement grid square
    value at the given row and col. Returns the number of cells modified.
    """
    # Must be within the bounds of the map and not already equal to fill
    if is_inside(map, row, col) and  map[row, col] != with_colour:
        return flood_fill(map, row, col, map[row, col], with_colour)
    return 0


def flood_fill(map: np.ndarray, row: int, col: int, replace: str, with_colour: str) -> int:
    """
    Performs flood fill, replacing replace with with_colour,
    starting from (row, col) and returns the number of cells changed.
    """
    # TODO: Implement this
    return 0


def main():
    map: np.ndarray # The character-based map
    command: list # User's entered command and parameters
    row: int # Command param for row
    col: int # Command param for col
    colour: str # Command param for colour

    # The initial map source.
    # Edit this to create some holes (or change its size)
    # Be sure to keep the new line chars (\n) at the end of all but the last line
    str_map = ("12345678912345678912\n"
               "12345678912345678912\n"
               "12345678912345678912\n"
               "12345678912345678912\n"
               "####################\n"
               "####################\n"
               "####################\n"
               "####################\n"
               "####################")

    map = create_map(str_map)

    display_bordered_title("Text Map")
    command = input("Enter commands (? for help). "
                    "There are no further prompts after this point.\n").split()

    while command != ["q"]:
        match command:
            # TODO: Make required changes in the appropiate cases
            case ["d"]: # Display
                display_map(map)
            case ["z"]: # Zoom
                command = input().split(' ')
                row = int(command[2])
                col = int(command[4])
                print(row)
                print(col)
                zoom(map,row,col)
            case ["r"]: # Replace
                print("Feature not implemented")
            case ["l"]: # Load
                print("Feature not implemented")
            case ["s"]: # Save
                print("Feature not implemented")
            case ["q"]: # Quit
                break
            case _:   # Unknown command. Will also capture ?
                display_help()

        # Wait for the next command
        command = input().split()


if __name__ == "__main__":
    main()
