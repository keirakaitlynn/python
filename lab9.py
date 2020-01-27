# 017675552
# Keira Wong
# Lab 09

def main():
    placings = ["United States", "Sweden", "Canada", "Great Britain", "Switzerland", "Norway", "South Korea", "Japan", "Italy", "Denmark"]
    country = ""
    medal = ""
    while country != "quit":
        country = input("Enter a country: ")
        for i in range(len(placings)):
            if placings[i] == country:
                place = i + 1
                if place == 1:
                    medal = "(Gold medal)"
                if place == 2:
                    medal = "(Silver medal)"
                if place == 3:
                    medal = "(Bronze medal)"
                print(country, "placed", place, medal)
                break
            else:
                place = 0
        if place == 0 and country != "quit":
            print(country, "did not compete")
        if country == "quit":
            print("Bye!")       
        
main()

# stone is a large polished, circular stone with a handle on top of it
# house are rings or circles towards where a play is directed
# button is a circle located at the center of the house
# sweeper is someone who moves back and forth in the path of a moving stone
# skip is the player that decides the strategy/directs the team
# 2. Norway
# 3. Biathlon
