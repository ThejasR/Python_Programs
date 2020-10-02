import ply.lex as lex
tokens = ('NUMBER', 'WORD')
#t_NUMBER = '\d+'
def t_NUMBER(t) :
	r'\d+'
	print(t.value)
t_WORD = r'\w+'
def t_newline(t) :
	r'\n'
	print("new line")
t_ignore = ' \t'
lexer = lex.lex()
lexer.input('1729 has 1 and 2\n and 7 and 9')
for t in lexer:
	pass