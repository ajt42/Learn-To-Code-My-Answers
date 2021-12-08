# Aaron Taylor, aaronjtaylor42@gmail.com
# DMOJ ccc02j2, AmeriCanadian
# INPUT: a string of lowercase letters
# american_word = input()
# OUTPUT: a string
# print(american_word)
# RULES:
# 1) if the input string is 'quit!', the program terminates
# 2) the input string has to be longer than 4 characters and consist of a consonant followed by 'or'
# 3) if the input string does not meet the above reqs, then prints the input string again


done = False

while not done:
    american_word = input()
    if american_word == 'quit!':
        done = True
    elif len(american_word) > 4 and not (american_word[-3] in 'aeiouy') and american_word[-2:] == 'or':
        print(american_word[:-2] + 'our')

    else:
        print(american_word)


