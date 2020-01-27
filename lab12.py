# Lab 12 (Part 1)
# 017675552
# Wong, Keira
# Prof. Song
# 18 November 2018

# 12.1 - sum of #s 1 to n

n = int(input("Enter in an integer: "))
print("The integer the user has entered is", n)
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of the numbers 1 to", n, "is", sum)

# 12.2 - sum of the square of all #s from 1 to n

n = int(input("Enter in an integer: "))
sum = 0
for i in range(1, n+1):
    sum += i**2
print("The sum of the square of all numbers from 1 to", n, "is", sum)

# 12.3 - 12.2 w/ while loop

n = int(input("Enter in an integer: "))
i = 0
sum = 0
while (i <= n):
    sum += i**2
    i += 1
print("Using the while loop, the sum of the square of all numbers from 1 to", n, "is", sum)
