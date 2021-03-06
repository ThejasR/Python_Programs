# anchor
import re


def mymatch(subjects, pat) :
	print('pattern : ', pat)
	for sub in subjects :
		m = re.search(pat, sub)
		if m :
			print(sub, ' : ', m.group())
	print('-' * 40)


subjects = [ 'cat', 'concat', 'cattle', 'catdogcat' ]
pat = 'cat' # match all
mymatch(subjects, pat)
pat = '^cat' # begin with
mymatch(subjects, pat)
pat = 'cat$' # end with
mymatch(subjects, pat)
pat = '^cat$' # just the cat
mymatch(subjects, pat)


# anchor : zero width pattern

# '^[^^]'
#	begin with anything other than a caret

# how to match rama - should be a word by itself
# rama
# rama krishna
# bala rama
# aaa rama bbb
# shd not match
# ramakrishna      
# balarama         
# aaaramabbb       


# 'rama'  match all
# 'rama ' will not match the first one
# '\brama\b'   \b : word boundary


subject = ['rama', 'rama krishna', 'bala rama', 'ramakrishna', 'aaaramabbb']
patt = '\brama\b'

mymatch(subject,patt)