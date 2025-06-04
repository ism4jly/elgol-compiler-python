import ply.yacc as yacc
from lexer.elgol_lexer import tokens

# Árvore sintática
def p_programa(p):
    '''programa : funcao bloco'''
    p[0] = ('programa', p[1], p[2])

def p_funcao(p):
    '''funcao : INTEIRO ID LPAREN parametros RPAREN DOT'''
    p[0] = ('funcao', p[2], p[4])

def p_parametros(p):
    '''parametros : parametro
                  | parametro COMMA parametros'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_parametro(p):
    '''parametro : INTEIRO ID'''
    p[0] = ('parametro', p[2])

def p_bloco(p):
    '''bloco : INICIO DOT comandos FIM DOT'''
    p[0] = ('bloco', p[3])

def p_comandos(p):
    '''comandos : comando
                | comando comandos'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_comando_atribuicao(p):
    '''comando : ID EQUALS expressao DOT'''
    p[0] = ('atribuicao', p[1], p[3])

def p_comando_atribuicao_elgio(p):
    '''comando : ELGIO EQUALS expressao DOT'''
    p[0] = ('atribuicao_elgio', p[3])

def p_comando_se(p):
    '''comando : SE expressao DOT comando senao_opcional FIM DOT'''
    p[0] = ('condicional', p[2], p[4], p[5])

def p_senao_opcional(p):
    '''senao_opcional : SENAO DOT comando
                      | vazio'''
    if len(p) == 4:
        p[0] = p[3]
    else:
        p[0] = None

def p_expressao_binaria(p):
    '''expressao : expressao PLUS expressao
                 | expressao MINUS expressao
                 | expressao TIMES expressao
                 | expressao DIVIDE expressao
                 | expressao GT expressao
                 | expressao LT expressao
                 | expressao EQUALS expressao'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expressao_termo(p):
    '''expressao : ID
                 | NUMBER'''
    p[0] = p[1]

def p_vazio(p):
    'vazio :'
    p[0] = None

def p_error(p):
    if p:
        print(f"\nErro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'\n")
    else:
        print("\nErro de sintaxe: fim inesperado do arquivo\n")

# Constrói o parser
parser = yacc.yacc()
