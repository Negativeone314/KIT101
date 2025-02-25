def display_message(message: str):
    """Display a message on the screen"""
    
    message = message.upper()
    print(f"***\n{message}\n***")


def get_sequence(message: str):
    """Get a sequence from the user"""
    
    return input(message).upper()


def show_complement(sequence: str):
    """Determines the complement of the sequence, then displays the sequence and the complement separated by bars"""
    
    sequence = sequence.upper()
    print(sequence)
    for i in range(len(sequence)):
        print("|", end="")
    print()
    print(match_sequence(sequence))


def data_cleaning(sequence: str):
    """Determines the percentage of errors in the sequence, and returns the cleaned sequence which only includes ATGC"""
    
    keep = "ATGC"
    result = ""
    number_of_errors = 0
    
    for character in sequence:
        if character in keep:
            result += character
        else:
            result += "."
            number_of_errors += 1
    
    error_percentage = number_of_errors / len(sequence) * 100
    error_percentage = round(error_percentage, 1)
    
    return result, error_percentage


def match_sequence(sequence: str):
    """Determines the complement of the sequence"""
    
    matching = ""
    
    for char in sequence:
        if char == "A":
            matching += "T"
        elif char == "T":
            matching += "A"
        elif char == "G":
            matching += "C"
        elif char == "C":
            matching += "G"
        else:
            matching += "."
    
    return matching


def transcribe_section(sequence: str, start_point: int, length: int):
    """Transcribes a given section of the sequence, which is to replace T with U"""
    
    section = sequence[start_point - 1:start_point + length - 1]
    transcribed = ""
    
    for char in section:
        if char == "T":
            transcribed += "U"
        else:
            transcribed += char
    
    return transcribed


def add_sequence(sequence: str):
    """Adds another sequence to the end of the sequence"""
    
    to_add = get_sequence("Enter another sequence: ")
    to_add = data_cleaning(to_add)[0]
    sequence += to_add
    return sequence


def present_options(sequence: str, percentage_error: float):
    choice = 0
    while choice != 6:
        print()
        print(f"The sequence is {sequence}.\n"
              "1. Display sequence and complement\n"
              "2. Display error rate\n"
              "3. Transcribe entire sequence\n"
              "4. Transcribe a section of the sequence\n"
              "5. Add another sequence to the end\n"
              "6. Quit\n")
        try:
            choice = int(input("Action: "))
            if 1 <= choice <= 5:
                match choice:
                    case 1:
                        show_complement(sequence)
                    case 2:
                        print(f"Error percentage is {percentage_error}%")
                    case 3:
                        print(f"{sequence} -> {transcribe_section(sequence, 1, len(sequence))}")
                    case 4:
                        start_point = input("Enter start point: ")
                        length = input("Enter the length of section you want to transcribe: ")
                        try:
                            start_point = int(start_point)
                            length = int(length)
                        except:
                            print("Both start point and length must be integers.")
                        
                        print(f"{sequence[start_point + 1:start_point + length + 1]} -> {transcribe_section(sequence, start_point, length)}")
                    case 5:
                        sequence = add_sequence(sequence)
            else:
                print("Choice out of range.")
        except:
            print("Invalid input")
    print("Exiting program...")