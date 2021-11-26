# DMOJ sac22cc1p1
# INPUT: three integers, each on a different line
# trick_or_treaters_number = int(input())
# candy_bar_given_per = int(input())
# total_amount_candy_bars = int(input())
# OUTPUT: the number of candy bars he has left
# leftover_candy_bars

trick_or_treater_number = int(input())
candy_bar_given_per = int(input())
total_amount_candy_bars = int(input())

total_candy_bars_given = trick_or_treater_number * candy_bar_given_per
leftover_candy_bars = total_amount_candy_bars - total_candy_bars_given

print(leftover_candy_bars)
