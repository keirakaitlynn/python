# Lab 4
# 017675552
# Keira Wong
# Prof. Terrell
# CECS 174 TuTh 10:30-11:45pm

def dep_value(orig_price, num_years):
    curr_value = orig_price - (orig_price * .18)
    i = 1
    while i in range(0, num_years + 1):
        print("After", i, "year(s), your car's value will be ${0:,.2f}".format(curr_value))
        i += 1
        curr_value = curr_value - (curr_value * .18)
while True:
    
    # User inputs the original price of their car (as a float)
    print()
    orig_price = float(input("Enter the car's original price: "))
    num_years = int(input("Enter the number of years: "))
    
    # User input must be positive
    if orig_price > 0 and num_years > 0:
        
        # Calculate depreciated value of car over the # of years
        
           
        # Calls function, given user input
        dep_value(orig_price, num_years)
        break
            
    # Reprompts user to enter valid input
    print()        
    print("ERROR: Invalid input, please try again.")

''' According to CarFax, the value of a new vehicle can drop "by about 14% per year on average."
If I was to purchase a new car at $5,552, this would mean that after one year of
ownership, my car would depreciate to at least

or

Using the Compound Interest Rate formula, where P, the value of the car, is $5,552 '''
