# ply : python lex and yacc
import ply.lex as lex
import ply.yacc as yacc
tokens = ( 'NUMBER', 'OP')
t_ignore= ' \t'
t_OP = '\+'
def t_NUMBER(t) :
	r'\d+'
	t.value = int(t.value)
	print (t.value, type(t.value))
	return t

def p_expr(p) :
		
lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse("25 + 36")
print(res)

# 25 + 36
# number op number

