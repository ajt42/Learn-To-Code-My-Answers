# DMOJ wc15c2j1
# INPUT: an integer
# OUTPUT: the sentence 'A long time ago in a galaxy far away...' with far * integer
# use the strip method to remove the final comma, especially when int = 1

how_many_fars = int(input())

a_new_hope_opening_scrawl = 'A long time ago in a galaxy' + ' ' + ('far, ' * how_many_fars).strip(', ') + ' ' + 'away...'

print(a_new_hope_opening_scrawl)
