
# smallest of three #s

number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))
def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    print("The smallest of the 3 numbers is : ", smallest_num)
smallest(number1, number2, number3)

# average of three #s

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))

# 5.16 odd even counter

import random

def isEven():
    count = 0
    odd = 0
    even = 0
    while count < 100:
        num = random.randrange(1, 101)
        count +=1
        print(num)
        if num % 2 != 0:
            even += 1
        else:
            odd += 1
    print('The # of times we get an odd # is', odd, 'and the # of times we get an even # is', even)
isEven()
