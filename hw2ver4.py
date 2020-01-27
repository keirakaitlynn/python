# Homework 02 Version 01
# CECS 174 TuTh
# 017675552
# Keira Wong

# IMPORT
import EnglishDictionary
import math

# INITIALIZATION
# a man, a plan, a canal, panama

# FUNCTIONS

# Print main menu to the screen
def print_menu():
    print("""
    Main menu:
    1. Is it a palindrome?
    2. Is it a crossword square?
    3. Quit
    """)

# Read the user's selected choice & validate it
def get_menu_choice():
    result = True
    while result == True:
        choice = int(input("Choose a function: "))
        if choice > 0 and choice < 4:
            return choice
            break
        else:
            continue

# Get user to input phrase, validate as having at least 1 char
def get_phrase():
    result = True
    while result == True:
        phrase = (input("Enter a phrase: "))
        if phrase != "":
            return phrase
            break
        else:
            continue

# Given a phrase, return True if phrase is a palindrome & False otherwise
def is_palindrome(phrase):

    # For each character, "i", in half the length of the given phrase
    for i in range((len(phrase)//2)):
        # j represents position of the character in the phrase at the other end (excluding non-alpha characters)
        j = -1 - i
        # If "i" is not a letter, skip over the character
        if ((phrase[i]).isalpha()) != True:
            i += 1
        # If each character, "i", is not equal to the letter opposite of "i" then phrase is not a palindrome
        if phrase[i] != phrase[j]:
            return False
        # Otherwise, phrase is a palindrome
        else:
            return True

# Implements Choice #1: "Check a phrase to see if it is a palindrome."
def menu_check_palindrome():
    phrase = get_phrase()
    palindrome = is_palindrome(phrase)
    if palindrome == True:
        print(phrase, "is a palindrome!")
    if palindrome == False:
        print(phrase, "is not a palindrome")

# User inputs the words of a word square, one per line
def get_crossword_square():
    result = ""
    first = input("Please enter the first word of the square: ")
    result = first
    # For each character in the given word, "first":
    for each_char in range(len(first)-1):
        second = input("Please enter the next word of the square: ")
        result += second
    return result

# Given concatenated string (a potential crossword square), "square", determine if string actually is a crossword square
def check_crossword_square(square):
    
    # INITIALIZATION
    squareLength = len(square) ## = 16
    # The "order" of the square is the square root of the length of the given concatenated string, "square"
    order = int((math.sqrt(squareLength))) ## = 4
    every_four_char = 0
    is_word_square = True
    each_char = every_four_char + 1
    vert_substr = ""
    
    for each_char in (range(squareLength)):
        while every_four_char in (range(squareLength)):

            # HORIZONTAL STRINGS: Identifies horizontal strings of square & determines if each horizontal string is a word
            # Each horizontal substring is the length of "order"
            each_horiz_substr = square[every_four_char:every_four_char+order]
            # If ANY substring that runs through is not in "EnglishDictionary", then substring is NOT a word HORIZONTALLY
            if EnglishDictionary.is_word(each_horiz_substr) == False:
                is_word_square = False
            
        # VERTICAL STRINGS: Identifies vertical strings of square & Determines if each vertical string is a word
            # "vert_substr" is set to the concatenation of vertical letters
            vert_substr += square[every_four_char]
            every_four_char += order
        # If ANY substring that runs through is not in "EnglishDictionary", then substring is NOT a word VERTICALLY
        if EnglishDictionary.is_word(vert_substr) == False:
            is_word_square = False

    # If horizontal or vertical substrings are not words, this function returns False.
    # Otherwise, this function returns True.
    return is_word_square

# Implements Choice #2: "Check a crossword square."
def menu_check_crossword_square():
    square = get_crossword_square()
    is_word_square = check_crossword_square(square)
    every_four_char = 0
    squareLength = len(square)
    order = int((math.sqrt(squareLength)))
    while every_four_char in (range(squareLength)):
            # HORIZONTAL STRINGS: Identifies horizontal strings of square & determines if each horizontal string is a word
            # Each horizontal substring is the length of "order"
            each_horiz_substr = square[every_four_char:every_four_char+order]
            print(each_horiz_substr)
            every_four_char += order
                
    if is_word_square == True:
        print("is a crossword square!")
    else:
        print("is not a crossword square.")
    
# Program Flow
def main():
    # Displays menu
    print_menu()
    # User inputs choice
    choice = get_menu_choice()
    if choice == 1:
        menu_check_palindrome()
    if choice == 2:
        menu_check_crossword_square()
    while choice != 3:
        print_menu()
        get_menu_choice()
    if choice == 3:
        exit()

# EXECUTES PROGRAM
main()
