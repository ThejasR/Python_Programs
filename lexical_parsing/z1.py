# ply : python lex and yacc
import ply.lex as lex
import ply.yacc as yacc
tokens = ( 'DIGIT', 'LETTER')
# specify the description of token
#	a) as a string
#	b) as a function (if there is some action)
t_DIGIT = '\d'
t_LETTER = '[a-zA-Z]'
t_ignore= ' \t'
# assignment : take care of offset
def t_newline(t) :
	r'\n'
	t.lexer.lineno += 1
# make a lex object
lexer = lex.lex()
lexer.input("""test 123
		456
	""")
for t in lexer:
	print(t)

