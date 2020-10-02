#re includes module-level functions for working with regular 
#expressions as text strings, but it is usually more efficient to 
#compile the expressions your program uses frequently. 
#The compile() function converts an expression string into a RegexObject.

import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print ('Looking for "%s" in "%s" ->' % (regex.pattern, text))

    if regex.search(text):
        print ('found a match!')
    else:
        print ('no match')