import re

sub = 'abcdefgh'
# number these based on left parenthesis
#      12   3    4 5
pat = '((..)(..))(.(..).)'
m = re.search(pat, sub)
if m :
	print('matched : ', m.group())
	print('matched : ', m.groups())
	print('matched : ', m.group(1))
	print('matched : ', m.group(2))
	print('matched : ', m.group(3))
	print('matched : ', m.group(4))
	print('matched : ', m.group(5))
