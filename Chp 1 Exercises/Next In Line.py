# Aaron Taylor, aaronjtaylor42@gmail.com
# #DMOJ ccc13j1 given the ages of the youngest and middle children, output age of oldest
# INPUT: two integers assigned to variables; youngest_child_age and middle_child_age
# OUTPUT: oldest child age
# get difference in age by subtracting middle from youngest; age_difference
# get oldest child age by adding age_difference to middle_child_age

youngest_child_age = int(input())
middle_child_age = int(input())

age_difference = middle_child_age - youngest_child_age

oldest_child_age = middle_child_age + age_difference

print(oldest_child_age)
