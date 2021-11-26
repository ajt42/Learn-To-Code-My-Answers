# DMOJ sac21ccp1
# INPUT: will be the original area of the rectangle without magnification/shrinkage
# OUTPUT: the area of the rectangle after shrinking it; integer

original_rectangle_area = int(input())
rectangle_area_after_shrinkage = original_rectangle_area // 40

print(rectangle_area_after_shrinkage)
