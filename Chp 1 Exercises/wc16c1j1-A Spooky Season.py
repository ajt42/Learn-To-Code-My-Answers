# DMOJ wc16c1j1 'A Spooky Season'
# Input: a line consisting of a single integer
# Output: a single line consisting of a single string - the spooky word
# corresponding to the integer input
# the inputted integer will multiply the letter 'o' by its value

how_many_os = int(input())

season_word = 'sp' + 'o' * how_many_os + 'ky'
print(season_word)
