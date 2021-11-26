# Aaron Taylor
# aaronjtaylor42@gmail.com
# 2021/11/23
# DMOJ ccc21j1, Boiling Water
# GOAL: calculate atmospheric pressure for a given when water boils
# atmospheric_pressure = 5 * temperature_water_boils - 400
# also determine if you are above, below, or at sea level
# INPUT: one line; integer; temperature_water_boils = int(input())
# temperature_water_boils must be >= 80 and <= 200
# OUTPUT: two lines; integers; atmospheric_pressure
# -1 = below sea level; 0 = at sea level; 1 = above sea level

temperature_water_boils = int(input())
atmospheric_pressure = 5 * temperature_water_boils - 400

if atmospheric_pressure < 100:
    print(atmospheric_pressure)
    print('1')
elif atmospheric_pressure > 100:
    print(atmospheric_pressure)
    print('-1')
else:
    print(atmospheric_pressure)
    print('0')

