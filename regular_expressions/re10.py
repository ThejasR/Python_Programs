import re

sub = 'bad teacher bad python bad re'
#pat = 'bad (\w+)'
pat = 'bad (\w+) bad (\w+) bad (\w+)'
m = re.search(pat, sub)
if m :
	print(m.groups())

print(re.findall('bad (\w+)', sub))
