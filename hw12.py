# Homework 12 (Part 1)
# 017675552
# Wong, Keira
# Prof. Song
# 18 November 2018

# 4.7 - Pennies for Pay

days = int(input('Enter the number of days: '))
print('Day\t\t', 'Salary')
print('-' * 25)
total = 0
for i in range(1, days + 1):
    salary = 0.01 * 2 ** (i -1)
    print(format(i, '3.0f'), '\t\t$', format(salary, '8.2f'))
    total += salary
print('The total pay at the end of the period is $', total)

# 4.8 - Sum of #s

number = float(input('Enter a positive number or enter a negative number '
                     'if you want to end: '))
total = 0
while number > 0:
    total += number
    number = float(input('Enter a positive number: '))
print('The sum is', total)
