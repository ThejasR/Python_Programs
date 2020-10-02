import re


def mymatch(subjects, pat) :
	print('pattern : ', pat)
	for sub in subjects :
		m = re.search(pat, sub)
		if m :
			print(sub, ' : ', m.group())
	print('-' * 40)

subjects = [ 'good food' ]
pat = 'o+' # match oo of good
mymatch(subjects, pat)
subjects = [ 'good food' ]
pat = 'o*' # match zero o before g; matches nothing successfully
mymatch(subjects, pat)

