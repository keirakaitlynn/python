# Lab 07
# 017675552
# Keira Wong
# CECS 174
# TuTh 3:30-4:20pm

# INITIALIZATION

import math

# User inputs an integer highway number
def get_interstate_number():
    interstate_number = -1
    while interstate_number <= 0:
        interstate_number = int(input("Please enter a US Interstate Highway route number: "))
    return interstate_number

# Function takes user input & determines whether # represents a primary interstate
def is_primary(interstate_number):
##    # ie. 10**n = num -> if n = 2, num = 100 & n + 1 would be the # of digits, 3
##    dig_interstate_num = int(math.log10(n))+1
    digits = 1
    while interstate_number >= 10:
        interstate_number /= 10
        math.floor(interstate_number)
        digits += 1
    # If there are less than 3 digits, the interstate # is a primary interstate
    if digits < 3:
        primary = True
    else:
        primary = False
    return primary

# Function takes a primary interstate # & determines its compass orientation
def compass_orientation(pr_interstate_number):
    if pr_interstate_number % 2 != 0:
        orientation = "north-south"
    else:
        orientation = "east-west"
    return orientation

# Function takes a primary interstate # & determines whether # represents a long-distance arterial highway
def is_arterial(pr_interstate_number):
    if pr_interstate_number % 5 == 0:
        arterial = True
    else:
        arterial = False
    return arterial

# Function takes an auxiliary interstate # & determines its type
def auxiliary_type(aux_interstate_number):
    # Takes the first digit of auxiliary interstate # & determines type based on whether digit is even or odd
    while aux_interstate_number >= 10:
        aux_interstate_number /= 10
    if math.floor(aux_interstate_number) % 2 == 0:
        type = "radial"
    else:
        type = "spur"
    return type

# Function takes an auxiliary interstate # & determines its parent
def parent_highway(aux_interstate_number):
    # Takes last two digits of auxiliary interstate #, assigned to variable "last_two"
    num = aux_interstate_number % 100
    last_two = math.floor(num)
    return last_two

# Program Flow
def main():
    highway_num = get_interstate_number()
    if is_primary(highway_num) == True:
        result = ""
        if is_arterial(highway_num) == True:
            result = "a long-distance arterial highway"
        print("Interstate", highway_num, "is", result, "oriented", compass_orientation(highway_num))
    else:
        print("Interstate", highway_num, "is a", auxiliary_type(highway_num), "highway of Interstate", parent_highway(highway_num))

# EXECUTION
main()
main()
main()
main()

# RESEARCH

# 1. Dwight Eisenhower // 2. I-95 // 3. Bellingham, Washington. It's about an ex.
