import ply.lex as lex

# Palavras-chave
reserved = {
    'inteiro': 'INTEIRO',
    'inicio': 'INICIO',
    'fim': 'FIM',
    'elgio': 'ELGIO',
    'se': 'SE',
    'senao': 'SENAO',
    'entao': 'ENTAO',
    'maior': 'MAIOR',
    'menor': 'MENOR',
    'igual': 'IGUAL',
    'diferente': 'DIFERENTE',
    'zero': 'ZERO',
    'comp': 'COMP',
}

# Tokens
tokens = [
    'ID',
    'FUNCTION_ID',
    'NUMBER',
    'EQUALS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'DOT',
    'COMMA',
    'LT',
    'GT'
] + list(reserved.values())

# Expressões regulares para tokens simples
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = r','
t_LT = r'<'
t_GT = r'>'

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Reconhece identificadores (nomes de variáveis)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra reservada
    return t

# Reconhece identificadores de função (ex: _Soma)
def t_FUNCTION_ID(t):
    r'_[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Reconhece números inteiros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Reconhece novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Trata caracteres ilegais
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()
