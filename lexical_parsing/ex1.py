import ply.lex as lex
import ply.yacc as yacc
tokens = ( 'DIGIT', 'LETTER')
t_DIGIT = r'\d'
t_LETTER = r'[a-zA-Z]'

lexer = lex.lex()
lexer.input('abc123')
for t in lexer :
	print (t)

