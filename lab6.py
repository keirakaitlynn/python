# Lab 06
# 017675552
# Keira Wong
# CECS 174
# TuTh 10:30-11:45pm
# Prof. Terrell

# INITIALIZATION
vowels_list = ["a","e","i","o","u"]

# FUNCTIONS

# User inputs a word
def get_word():
    word = input("Please enter a word: ")
    return word

# Asks if a given letter is a vowel
def is_vowel(letter):
    if letter in vowels_list:
        return True
    else:
        return False

# Counts # of times a letter switches from a vowel to a consonant
def calculate_measure(word):
    i = 0
    count = 0
    while i < len(word):
        if is_vowel(word[i-1]) == True and is_vowel(word[i]) != True:
            count += 1
        i += 1
    return count

# Program Flow
def main():
    print()
    word = get_word()
    measure = calculate_measure(word)
    print(word, "has a measure of", measure)
    print()
    
# EXECUTES PROGRAM
main()
main()
main()
