# multiple char regex
# * :
#	shell: any char repeated 0 or more times
#	re : closure
#		zero or more of what precedes it
# + : re : positive closure
#		one or more of what precedes it



import re

def mymatch(subjects, pat) :
	print('pattern : ', pat)
	for sub in subjects :
		m = re.search(pat, sub)
		if m :
			print(sub, ' : ', m.group())
	print('-' * 40)


subjects = [ 'ab*d', 'abcd', 'ad', 'abbbd', 'abbbbbbbbd', 'abbbbbd', 'abbbbd', 'cad', 'xxadyy' ]
pat = 'ab*d'
mymatch(subjects,pat)

pat = 'ab+d'
mymatch(subjects,pat)

pat = 'ab{3}d'
mymatch(subjects,pat)

pat = 'ab{3,5}d'
mymatch(subjects,pat)

# ab{3}d   => abbbd  : counting closure
# ab{3,5}d => abbbd | abbbbd | abbbbbd 
