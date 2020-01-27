# 017675552
# Keira Wong
# CECS 174
# TuTh 3:30-4:20pm
# Lab 5

# Asks user to input the magnitude for the given earthquake
def get_magnitude(num):
    while num > 0:
        magnitude = float(input("Please enter in the magnitude of earthquake {0}: "
                                .format(num)))
        # Input must be positive
        if magnitude > 0:
            return magnitude
        else:
            continue

# Assumes magnitude1 > magnitude2 & Calculates f, how many times stronger m1 was than m2
def compare_magnitudes(magnitude1, magnitude2):
    f = float(10 ** (1.5 * (magnitude1 - magnitude2)))
    return f

# Asks user if they want to compare 2 more earthquakes
def get_run_again():
    num = int(input("Try again? Type 1 for yes: "))
    if num == 1:
        return True
    else:
        return False

# Program flow
def main():
    result = True
    while result == True:
        # Calls get_magnitude twice & saves them as variables
        m1 = (get_magnitude(1))
        m2 = (get_magnitude(2))
        if m1 > m2:
            f = '{0:.1f}'.format(compare_magnitudes(m1, m2))
            print("An earthquake of magnitude", str(m1), "is", f, "times more powerful then an earthquake of magnitude", str(m2))
        if m2 > m1:
            f = '{0:.1f}'.format(compare_magnitudes(m2, m1))
            print("An earthquake of magnitude", str(m2), "is", f, "times more powerful than an earthquake of magnitude", str(m1))
        result = get_run_again()
        
main()

# Questions
# 1. Magnitude
# (a) 2011 Tohoku earthquake, Japan: 9.1
# (b) 1989 Loma Prieta earthquake, San Francisco, USA: 6.9
# (c) 2010 Haiti earthquake: 7.0
# 2. What is the relative strength difference of the 2011 Tohoku earthquake vs. the 2010 Haiti earthquake?
#       An earthquake of magnitude 9.1 is 1412.5 times more powerful then an earthquake of magnitude 7.0
# 3. Tohoku: 22,000
#    Haiti: 316,000
# yes
