# Aaron Taylor, aaronjtaylor42@gmail.com
# DMOJ ccc20j2, Epidemiology
# Learn To Code Chp 4, Indefinite Loops - use while loop
# GOAL: output an integer representing the first day the total number is greater than P
# INPUT: three integers on three lines;
# total number of people with disease; total_people = int(input())
# the number of people with disease; number_infected_people = int(input())
# number of people infected after being exposed; infection_rate = int(input())
# OUTPUT: an integer
# representing how many days until number_infected_people !<= total_people
# a person can only infect someone else once and ONLY on the very next day


total_people = int(input())
number_infected_people = int(input())
infection_rate = int(input())


days = 0
previous_day_infected = number_infected_people

while number_infected_people <= total_people:
    number_infected_people = number_infected_people + previous_day_infected * infection_rate
    previous_day_infected = previous_day_infected * infection_rate
    days += 1


print(days)
