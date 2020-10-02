import re
#returns match object
print(re.match(r'dog', 'dog cat dog'))

match = re.match(r'dog','dog cat dog')
print(match.group(0))
#print(match.group(1))

match = re.match(r'cat','dog cat dog')
print(match.group(0))

#match is at beginning of the string only 

