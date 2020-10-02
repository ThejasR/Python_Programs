import ply.lex as lex
import ply.yacc as yacc
tokens = ( 'ID', 'NUMBER', 'OP')
t_OP = r'[+-]'
t_ignore = ' \t'
def t_ID(t) :
	'[a-zA-Z]\w*'
	print ("token encountered : ", t.value)
	return t

def t_NUMBER(t) :
	'\d+'
	t.value = int(t.value)
	return t

lexer = lex.lex()
lexer.input('abc + 123 - pqr')
for t in lexer :
	print (t)

