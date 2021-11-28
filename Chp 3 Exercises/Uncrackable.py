# Aaron Taylor
# aaronjtaylor42@gmail.com
# 2021/11/23
# DMOJ wc17c3j3, Uncrackable
# Goal: to assess an inputted string as for whether or not it meets certain conditions
# INPUT: a string assigned to the variable; password = input()
# Constraints:
# Must be between (> 7) 8 and 12 characters (< 13)
# if len(password) > 7 or len(password) < 13
# string must contain at least 3 lowercase, 2 uppercase, and 1 digit
# need counter variable for each: lowercase, uppercase, and digit

password = input()
digits_allowed = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
lowercase_letters = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
uppercase_letters = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'

digit_count = 0
uppercase_count = 0
lowercase_count = 0

for char in password:
    if char in digits_allowed:
        digit_count += 1
    elif char in lowercase_letters:
        lowercase_count += 1
    elif char in uppercase_letters:
        uppercase_count += 1

if digit_count >= 1 and lowercase_count >= 3 and uppercase_count >= 2 and (len(password) > 7 and len(password) < 13):
    print('Valid')

else:
    print('Invalid')
