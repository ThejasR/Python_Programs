# how to simulate * of shell in regex => .* 
# Rules:
# 1. leftmost
# 2. eager : satisfy the eagerness
# 3. greedy : then become greedy
#	re engine backtracks to match the remaining pattern

#	to make the match non-greedy, we use a question mark
#	following the closure symbol


import re


def mymatch(subjects, pat) :
	print('pattern : ', pat)
	for sub in subjects :
		m = re.search(pat, sub)
		if m :
			print(sub, ' : ', m.group())
	print('-' * 40)


subjects = [ 'axxxbyyybzzz' ]
pat = 'a.*b' # greedy axxxbyyyb
mymatch(subjects,pat)
pat = 'a.*?b' # non greedy axxxb
mymatch(subjects,pat)

