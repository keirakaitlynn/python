# Homework 1
# 017675552s
# Keira Wong
# CECS 174 TuThu 3:30-4:20pm
# Prof. Terrell

import math

# Declare constants (light speed, # of meters equivalent to one light year, etc.)
LIGHT_SPEED = 299792458
METERS_PER_LY = (9.4607304725808 * (10**15))
DAYS_PER_YEAR = 365.2422
SECONDS_PER_YEAR = 31557600

# Display menu
ans = True
while ans:
    print("""
    1.Warp Speed
    2.Cost of Launch
    3.Time Dilation
    4.Quit
    """)
    ans = int(input("Select a function: "))
    # 1. Calculate Warp Speed
    if ans == 1:
        # User inputs speed (in warp factor units)
        speed_wf = float(input("Enter warp factor: "))
        # Inputed speed (in warp factor units) must be nonnegative
        while speed_wf <= 0:
            print()
            print("ERROR: Please enter a valid number.")
            print()
            speed_wf = float(input("Enter warp factor: "))
        # Convert speed (in warp factor units) to speed (in m/s)
        speed_ms = (speed_wf ** (10/3)) * LIGHT_SPEED
        # Print original speed & converted speed
        print("\nOriginal Speed: ", speed_wf, "warp factor")
        print("Converted Speed: ", "{0:,.2f}".format(speed_ms), "m/s")
    # 2. Calculate Cost of Launch
    elif ans == 2:
        # User inputs satellite's mass (kg) & satellite's manufacture cost ($)
        mass = float(input("Enter the satellite's mass (kg): "))
        manufacture_Cost = float(input("Enter the satellite's manufacture cost: $"))
        # Inputed mass (kg) & manufacture cost ($) must be positive
        while mass <= 0 or manufacture_Cost <= 0:
            print()
            print("ERROR: Please enter valid numbers.")
            print()
            mass = float(input("Enter the satellite's mass (kg): "))
            manufacture_Cost = float(input("Enter the satellite's manufacture cost: $"))
        # Calculate cost to launch through ULA
        ULA_PRICE_per_KG = 14830
        ula = ULA_PRICE_per_KG * mass
        # Calculate cost to launch through Space X
        X_PRICE_per_KG = 2720
        X_INSURANCE_PERCENTAGE_of_MC = .3
        space_x = (X_PRICE_per_KG * mass) + (X_INSURANCE_PERCENTAGE_of_MC * manufacture_Cost)
        # Compare the cost to launch between ULA & Space X
        print("ULA: $", ula)
        print("Space X: $", space_x)
        if ula > space_x:
            highest_Price = ula
            cheapest_Option = "Space X"
            cheapest_Price = space_x
        elif space_x > ula:
            highest_Price = space_x
            cheapest_Option = "ULA"
            cheapest_Price = ula
        else:
            print("\nBoth launch providers produce the same cost")
            break
        money_Saved = highest_Price - cheapest_Price
        print()
        print(cheapest_Option, "will save you $", "{0:,.2f}".format(money_Saved))
    # 3. Calculate Time Dilation
    elif ans == 3:
        # User inputs ship's speed (as a fraction of light speed, LS) & ship's distance (light years, LY)
        fraction_LS = float(input("Enter the speed of your space ship (as a fraction of c): "))
        ship_distance_LY = float(input("Enter the distance your space ship is traveling (light years): "))
        # Inputted speed must be between 0 and 1 & distance of the user's ship must be positive
        while fraction_LS <= 0 or fraction_LS >= 1 or ship_distance_LY <= 0:
            print()
            print("ERROR: Please enter valid numbers.")
            print()
            fraction_LS = float(input("Enter the speed of your space ship (as a fraction of c): "))
            ship_distance_LY = float(input("Enter the distance your space ship is traveling (light years): "))
        ship_speed = fraction_LS * LIGHT_SPEED
        # Convert the ship's speed from light years to meters
        ship_distance_M = ship_distance_LY * METERS_PER_LY
        # Calculate the time it takes for the ship to travel according to Earth
        time_seconds_E = ship_distance_M / ship_speed
        time_minutes_E = time_seconds_E / 60
        time_hours_E = time_minutes_E / 60
        time_days_E = time_hours_E / 24
        leftover_days_E = time_days_E % DAYS_PER_YEAR
        time_years_E = time_days_E / DAYS_PER_YEAR
        if time_days_E < DAYS_PER_YEAR:
            print()
            print("An observer on Earth ages", math.floor(time_days_E), "days during the trip.")
        else:
            print()
            print("An observer on Earth ages", int(time_years_E), "year(s),", math.floor(leftover_days_E), "days during the trip.")
        # Calculate the time it takes for the ship to travel (according to the ship)
        v_Squared = ship_speed ** 2
        c_Squared = LIGHT_SPEED ** 2
        dilation = math.sqrt(1 - (v_Squared / c_Squared))
        time_seconds_S = dilation * time_seconds_E
        # Convert the time it takes for the ship to travel (according to the ship) from seconds to years & days
        time_minutes_S = time_seconds_S / 60
        time_hours_S = time_minutes_S / 60
        time_days_S = time_hours_S / 24
        leftover_days_S = time_days_S % DAYS_PER_YEAR
        time_years_S = time_days_S / DAYS_PER_YEAR
        if time_days_S < DAYS_PER_YEAR:
            print()
            print("A passenger on the ship ages", math.floor(time_days_S), "days during the trip.")
        else:
            print()
            print("A passenger on the ship ages", int(time_years_S), "year(s),", math.floor(leftover_days_S), "days during the trip.")
    # 4. Quit
    elif ans == 4:
        print("\n Goodbye") 
        ans = None
    else:
        ans = False
        
# Inputted number must be a number between 1 and 4, inclusive.
while ans == False:
    print()
    print("ERROR: Invalid choice, pleast select an option below.")
    print("""
    1.Warp Speed
    2.Cost of Launch
    3.Time Dilation
    4.Quit
    """)
    ans = int(input("Select a function: "))
