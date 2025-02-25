"""
Program that creates a matching pattern of DNA
"""

__Author__ = "Thomas Couser"

import functions as fn


def main():
    fn.display_message("Welcome to the DNA Matching Program")
    
    sequence = fn.get_sequence("Enter a DNA sequence: ")
    
    sequence = fn.data_cleaning(sequence)[0]
    percentage_error = fn.data_cleaning(sequence)[1]
    
    fn.present_options(sequence, percentage_error)
    

if __name__ == "__main__":
    main()
