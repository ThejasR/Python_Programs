import re
match=re.search(r'dog', 'dog cat dog')
print(match)
print(match.group(0))


match=re.search(r'cat', 'dog cat dog')
print(match)
print(match.group(0))