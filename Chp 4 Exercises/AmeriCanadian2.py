# Aaron Taylor, aaronjtaylor42@gmail.com
# DMOJ ccc02j2, AmeriCanadian
# This is a slightly different solution to the problem, and I personally like this one better
# INPUT: a string of lowercase letters
# american_word = input()
# OUTPUT: a string
# RULES:
# 1) if the input string == 'quit!', the program terminates
# 2) the input string has to be longer than 4 characters and consist of a consonant followed by 'or'
# 3) if the input string does not meet the above reqs, then prints the input string again

done = False

consonants_lowercase = 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z'

while not done:
    american_word = input()
    if american_word == 'quit!':
        done = True

    elif len(american_word) > 4 and (american_word[-3] in consonants_lowercase) and american_word[-2:] == 'or':
        canadian_word = american_word[:-2] + 'our'
        print(canadian_word)

    else:
        print(american_word)
