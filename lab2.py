# 017675552
# Keira Wong
# Lab 02

# Ask the user to input player's name
name = input("Enter your full name: ")
print()

# Ask user to enter values and save under variables
plates = int(input("# of Plate Appearances: "))
bats = int(input("# of At Bats: "))
walks = int(input("# of Walks: "))
singles = int(input("# of Singles: "))
doubles = int(input("# of Doubles: "))
triples = int(input("# of Triples: "))
runs = int(input("# of Home runs: "))
print()

# Print player's total # of hits
hits = singles + doubles + triples + runs
print("Total # of Hits: ", hits)
print()

# Calculate & print player's Batting Average, round to nearest thousandth
batting_Average = hits / bats
print("{0:.3f}".format(batting_Average), " AVG")

# Calculate & print player's Slugging Percentage, round to nearest thousandth
slugging_Percentage = ((singles * 1) + (doubles * 2) + (triples * 3) + (runs * 4)) / bats
print("{0:.3f}".format(slugging_Percentage), " SLG")

# Calculate & print player's OPS, rount to nearest thousandth
on_Base_Percentage = (hits + walks) / plates
obp_Plus_Slugging = on_Base_Percentage + slugging_Percentage
print("{0:.3f}".format(obp_Plus_Slugging), " OPS")

# Q: What baseball player has the all time highest career OPS statistic?
# A: Babe Ruth
# Q: What baseball player has the highest career OPS statistic among active players?
# A: Mike Trout
