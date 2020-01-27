# Lab 14 Ch 8 Pt 2
# 017675552
# Wong, Keira
# Prof. Song

# 8.2. Sum of Digits In a String

def read():
    numbers = input('Enter a series of single-digit numbers with nothing'
                    'separating them: ')
    total = 0
    for i in numbers:
        total += int(i)
    print(total)
read()

# 8.11 Word Separator

my_string = "StopAndSmellTheRoses"
i = 0
result = ""
for c in my_string:
    if c.isupper() and i > 0:
        result += " "
        result += c.lower()
    else:
        result += c
    i += 1

print result
