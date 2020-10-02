import ply.lex as lex
import ply.yacc as yacc
tokens = ( 'ID', 'NUMBER', 'OP')
t_OP = r'\+'
t_ignore = ' \t'

def t_NUMBER(t) :
	'\d+'
	t.value = int(t.value)
	return t

def p_expr(p) :
	'expr : NUMBER'
	p[0] = p[1]
def p_expr_plus(p) :
	'expr : expr OP expr'
	p[0] = p[1] + p[3]	

lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse('20 + 30')
print (res)

