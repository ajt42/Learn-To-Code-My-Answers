# DMOJ wc18c3j1
# GOAL: to output the total number of pokedollars made with supplies and selling
# INPUT: three integers
# litres_of_paint = int(input())
# paint_needed_per_bottlecap = int(input())
# pokedollar_worth_per_bottlecap = int(input())
# OUTPUT: an integer representing the profits; profits_in_pokedollars

litres_of_paint = int(input())
paint_needed_per_bottlecap = int(input())
pokedollar_worth_per_bottlecap = int(input())

bottlecaps_produced = litres_of_paint // paint_needed_per_bottlecap # throws away remainder and rounds down
bottlecaps_produced_profit = bottlecaps_produced * pokedollar_worth_per_bottlecap
leftover_paint = litres_of_paint % paint_needed_per_bottlecap # modular division to get remainder value
leftover_paint_profit = leftover_paint * 1

profits_in_pokedollars = leftover_paint_profit + bottlecaps_produced_profit

print(profits_in_pokedollars)
