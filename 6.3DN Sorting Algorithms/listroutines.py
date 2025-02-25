"""
A collection of sorting algorithms for comparison with in-built sorting functions.
"""

__author__ = "James Montgomery, Lawrence Sambrooks, YOUR NAME"


def linear_search(data: list[int], target: int) -> int:
    """
    Performs a linear search for the location of a value in the list;
    returns -1 if it is not present.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Linear_search
    """
    found: bool = False
    index: int = -1
    counter: int = 0

    while counter < len(data) and not found:
        if data[counter] == target:
            found = True
            index = counter
        else:
            counter += 1

    return index


def binary_search(data: list[int], target: int) -> int:
    """
    Performs a binary search to find the position of the target;
    returns -1 if it is not in the list.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Binary_search
    """
    found: bool = False
    low: int = 0
    high: int = len(data) - 1
    middle: int
    index: int = -1

    while low <= high and not found:
        middle = (low + high) // 2
        if data[middle] == target:
            found = True
            index = middle
        else:
            if target < data[middle]:
                high = middle - 1
            else:
                low = middle + 1

    return index


def insertion_sort(data: list[int]):
    """
    Sorts the list into ascending order using insertion sort.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Insertion_sort
    """
    key: int # value to "insert"
    position: int # where to "insert"

    for i in range(1, len(data)):
        key = data[i]
        position = i
        # Shift larger values to the right
        while position > 0 and data[position-1] > key:
            position -= 1
        data.insert(position, data.pop(i))


def selection_sort(data: list[int]):
    """
    Sorts the list into ascending order using selection sort.
    See this Wikipedia article: https://en.wikipedia.org/wiki/Selection_sort
    """
    min: int
    temp: int

    for i in range(0, len(data)-1):
        min = i
        for scan in range(i+1, len(data)):
            if data[scan] < data[min]:
                min = scan
        # Swap the values
        data[min], data[i] = data[i], data[min]


def bubble_sort(data: list[int]):
    """
    Sorts the list into ascending order using bubble sort.
    """
    temp: int
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data


def display(data: list[int]):
    """
    Displays the values stored in a list of ints.
    """
    for i, val in enumerate(data):
        print(f"element {i}: {val}") # the formatting is up to you

