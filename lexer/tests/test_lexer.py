from lexer.elgol_lexer import lexer

# Código Elgol de teste
codigo_fonte = """
inteiro _Maior(inteiro A, inteiro B).
inicio.
    se A > B.
        Resultado = A.
    senao.
        Resultado = B.
    fim.
elgio = Resultado.
fim.
"""

# Alimente o analisador léxico
lexer.input(codigo_fonte)

# Imprime tokens encontrados
for tok in lexer:
    print(f"{tok.type:<15} -> {tok.value}")
