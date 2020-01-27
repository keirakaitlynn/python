# 017675552
# Wong, Keira
# Prof. Song
# November 28

# Chapter 8.1 Initials

def get_name():
    first = input('Enter your first name: ')
    middle = input('Enter your middle name: ')
    last = input('Enter your last name: ')
    print(first[0].upper(), '.', middle[0].upper(), '.', last[0].upper(), '.', sep='')
get_name()

# Chapter 8.3 Date Printer

def read():
    date = input('Enter a date in the form mm/dd/yyyy: ')
    mm = date[0:2]
    if mm == '01':
        month = 'January'
    elif mm == '02':
        month = 'February'
    elif mm == '03':
        month = 'March'
    elif mm == '04':
        month = 'April'
    elif mm == '05':
        month = 'May'
    elif mm == '06':
        month = 'June'
    elif mm == '07':
        month = 'July'
    elif mm == '08':
        month = 'August'
    elif mm == '09':
        month = 'September'
    elif mm == '10':
        month = 'October'
    elif mm == '11':
        month = 'November'
    elif mm == '12':
        month = 'December'
    print(month, date[3:5]+',', date[6:10])
read()

# 8.9 Vowels & Consonants

def calc_num_vowels(string):
    vowels = 'aeiou'
    num_vowels = 0
    for ch in string:
        if ch.lower() in vowels:
            num_vowels += 1
    return num_vowels
   
def calc_num_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    num_consonants = 0
    for ch in string:
        if ch.lower() in consonants:
            num_consonants += 1
    return num_consonants

users_string = input('Enter a string of characters: ')

vowels = calc_num_vowels(users_string)
consonants = calc_num_consonants(users_string)

print('Your string has', vowels, 'vowels and', consonants, 'consonants.')

def calc_num_vowels(string):
    vowels = 'aeiou'
    num_vowels = 0
    for ch in string:
        if ch.lower() in vowels:
            num_vowels += 1
    return num_vowels
    
def calc_num_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    num_consonants = 0
    for ch in string:
        if ch.lower() in consonants:
            num_consonants += 1
    return num_consonants

users_string = input('Enter a string of characters: ')

vowels = calc_num_vowels(users_string)
consonants = calc_num_consonants(users_string)

print('Your string has', vowels, 'vowels and', consonants, 'consonants.')
