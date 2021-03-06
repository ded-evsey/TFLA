from ply import lex
import ply.yacc as yacc
import math
tokens = (
    'PLUS',
    'PERCENT',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'SQRT'
)

t_ignore = ' \t'

t_PLUS    = r'\+'
t_PERCENT = r'\#'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SQRT = r'sqrt'

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'PERCENT' ),
    ( 'left', 'TIMES', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)

def p_add( p ) :
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]

def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]

def p_percent( p ) :
    'expr : expr PERCENT expr'
    p[0] = (p[1]/p[3])*100

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]

def p_mult_div( p ) :
    '''expr : expr TIMES expr
            | expr DIV expr'''

    if p[2] == '*' :
        p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]

def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_SQRT(p):
    'expr : SQRT LPAREN expr RPAREN'
    p[0] = math.sqrt(p[3])

def p_error( p ):
    print("Syntax error in input!")


parser = yacc.yacc()
if __name__ =='__main__':
    print("Выражение для рассчёта : sqrt(3#6+3#6)")
    res = parser.parse("sqrt(3#6+3#6)")
    print("Результат выражения: ", res)