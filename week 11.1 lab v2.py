# 017675552
# Wong, Keira
# Prof. Song
# 8 November 2018

# 4.3 Budget Analysis
budget = float(input('Please input the amount of your budget: $'))
total = 0
another = 'y'
while another == 'y' or another == 'Y':
    expense = float(input('Please input the amount of your expense: $'))
    total += float(expense)
    another = input('Do you want to enter another expense? Enter y for yes or any key for no:')
print("Your budget is ", budget - total)

# Sum of Numbers 1-101 divisible by 5 (using While Loop)
number = 1
total = 0
print("Numbers between 1 and 101 that are divisible by 5: ")
while (number >= 1 and number <= 101):
    if (number%5 == 0):
        print(number)
        total += number
    number += 1
print("Sum of Numbers 1-101 divisible by 5 = ", total)

# Sum of Every Third Number from 1-1001 (using While Loop)
# ie. (1 + 4 + 7 + 10 + ...)
number = 1
total = 0
print("Every third number between 1 and 1001: ")
while(number >= 1 and number <= 1001):
    print(number)
    number += 3
total += number
print("Sum of Every Third Number from 1-1001 is ", total)
