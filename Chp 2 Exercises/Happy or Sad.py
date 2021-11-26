# DMOJ ccc15j2
# GOAL: write a program to determine overall mood of message
# INPUT: one line that contains a string of characters
# message = input()
# OUTPUT: mood_of_message
# assign .count() to variables that represent target
# if the input line does not contain any happy or sad emots = none
# if the input contains an equal number of happy and sad emots = unsure
# if the input contains happy > sad emots = happy
# if the input contains sad > happy emots = sad

message = input()

happy_emoticon_amount = message.count(':-)')
sad_emoticon_amount = message.count(':-(')

if happy_emoticon_amount == 0 and sad_emoticon_amount == 0:
    print('none')
if happy_emoticon_amount > sad_emoticon_amount:
    print('happy')
if sad_emoticon_amount > happy_emoticon_amount:
    print('sad')
if happy_emoticon_amount == sad_emoticon_amount:
    print('unsure')


