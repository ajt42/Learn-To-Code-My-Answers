# Aaron Taylor, aaronjtaylor42@gmail.com
# DMOJ coci13c3p1, Riječi
# GOAL: to write a program that outputs the nums of A & B after K button presses
# INPUT: an integer representing the num of button presses;
# number_of_button_presses = int(input())
# OUTPUT: two integers representing the number of letters;
# number_of_As, number_of_Bs; print(number_of_As, number_of_Bs)
# have a counter variable or in range loop
# Initial state of machine, k = 0: A
# After k = 1 button press: A -> B
# k = 2, B -> B A
# k = 3, B A -> BA B
# k = 4, B A B -> BA B BA
# Button transforms all B -> BA and all A -> B

number_of_button_presses = int(input())
number_of_As = 1
number_of_Bs = 0

for i in range(number_of_button_presses):
    new_number_of_As = number_of_Bs
    new_number_of_Bs = number_of_As + number_of_Bs
    number_of_As =  new_number_of_As
    number_of_Bs = new_number_of_Bs

print(new_number_of_As, new_number_of_Bs)
