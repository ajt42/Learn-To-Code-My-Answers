# Aaron Taylor, aaronjtaylor42@gmail.com
# 2021/11/25
# DMOJ CCC11S1, English or French
# GOAL: to distinguish English input text from French input text
# INPUT: first is int representing num of sents; number_of_sentences = int(input())
# INPUT 2: N amount of strings; sentences = input()
# OUTPUT: print('English') or print('French')
# Rules for distinguishing between Eng and French
# If text has more 't' and 'T' chars than 's' and 'S', probably English
# If text has more 's' and 'S' than 't' and 'T', probably French
# If number of 't' and 'T' chars = 's' and 'S' chars, probably French

number_of_sentences = int(input())
t_amount = 0
T_amount = 0
s_amount = 0
S_amount = 0

for i in range(number_of_sentences):
    sentences = input()
    for i in range(len(sentences)):
        if sentences[i] == 't':
            t_amount += 1
        elif sentences[i] == 'T':
            T_amount += 1
        elif sentences[i] == 's':
            s_amount += 1
        elif sentences[i] == 'S':
            S_amount += 1

if t_amount + T_amount > s_amount + S_amount:
    print('English')
elif t_amount + T_amount < s_amount + S_amount:
    print('French')
elif t_amount + T_amount == s_amount + S_amount:
    print('French')

