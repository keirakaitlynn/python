# Lab 10 (Part 2)
# 017675552
# Wong, Keira
# 5 November 2018

# 2.12 Stocks
numberofSharesPurchased = 2000
amountPaidPerShare = 40.00
amountPaidForStock = numberofSharesPurchased * amountPaidPerShare
commissionForBuying = 0.03 * amountPaidForStock
numberOfSharesSold = 2000
amountSoldPerShare = 42.75
amountReceivedForStock = numberOfSharesSold * amountSoldPerShare
commissionForSelling = 0.03 * amountReceivedForStock
profit = (amountReceivedForStock - commissionForSelling ) - \
         (amountPaidForStock - commissionForBuying )
print("Amount paid for stock: $" + format( amountPaidForStock, ",.2f" ), \
      "Commission for buying: $" + format( commissionForBuying, ",.2f" ), \
      "Amount received for stock: $" + \
      format( amountReceivedForStock, ",.2f" ), \
      "Commission for selling: $" + format ( commissionForSelling, ",.2f" ), \
      "Profit: $" + format(profit, ",.2f" ),)

# 3.1 Day of the Week
number = int(input('Please input a number in the range of 1 through 7: '))

if number == 1:
    print('Monday')
elif number == 2:
    print('Tuesday')
elif number == 3:
    print('Wednesday')
elif number == 4:
    print('Thursday')
elif number == 5:
    print('Friday')
elif number == 6:
    print('Saturday')
elif number ==7:
    print('Sunday')
else:
    print('Error')
    
# 3.2 Areas of Rectangles

length_a = float(input('Please input the length of rectangle a: '))
width_a = float(input('Please input the width of rectangle a: '))
length_b = float(input('Please input the length of rectangle b: '))
width_b = float(input('Please input the width of rectangle b: '))
area_of_a = length_a * width_a
area_of_b = length_b * width_b

if area_of_a > area_of_b:
    print('Rectangle a has the greater area.')
elif area_of_b > area_of_a:
    print('Rectangle b has the greater area.')
else:
    print('Rectangle a and b has the same area.')

# 3.13 Shipping Charges

weight = int(input('Please enter the weight of a package you leave in pound: '))

if weight > 10:
    print('The shipping charge is $4.75')
elif weight <= 10 and weight > 6:
    print('The shipping charge is $4.00')
elif weight <= 6 and weight > 2:
    print('The shipping charge is $3.00')
else:
    print('The shipping charge is $1.50')
