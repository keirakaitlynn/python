# Lab 15
# 017675552
# Wong, Keira
# Prof. Song

# 5.1 Kilometer Converter

km = float(input('Enter a distance in kilometers: '))
def convert(km):
    miles = km * 0.6214
    print(format(miles, '.2f'), 'miles')
    
convert(km)

# 5.10 Feet to Inches

feet = float(input('Enter a number of feet: '))

def conver(feet):
    inches = feet * 12
    print(feet, 'feet is ', inches, 'inches')

conver(feet)

# 5.12 Maximum of Two Values

a = int(input('Enter a integer: '))
b = int(input('Enter another integer: '))
def max(a, b):
    if a > b:
        print(a, 'is bigger than', b)
    else:
        print(b, 'is bigger than', a)
max(a, b)
