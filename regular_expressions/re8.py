import re


def mymatch(subjects, pat) :
	print('pattern : ', pat)
	for sub in subjects :
		m = re.search(pat, sub)
		if m :
			print(sub, ' : ', m.group())
	print('-' * 40)

subjects = [ 'hello' ]
# match if two consecutive chars are same
pat = '..'   #he
mymatch(subjects,pat)


