# DMOJ wc17c1j2
# Goal: to write a program that converts from Celsius to Fahrenheit
# INPUT: an integer representing Celsius
# OUTPUT: an integer representing Fahrenheit
# FORMULA: degrees_celsius= 5/9 * (degrees_fahrenheit - 32)
# rearranged formula: (degrees_celsius) / (5/9) + 32 = degrees_fahrenheit

degrees_celsius = int(input())
degrees_fahrenheit = ((degrees_celsius) / (5/9)) + 32

print(degrees_fahrenheit)
