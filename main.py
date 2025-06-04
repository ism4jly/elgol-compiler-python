from lexer.elgol_lexer import lexer
from parser.elgol_parser import parser

with open("examples/exemplo1.elgol", encoding="utf-8") as f:
    data = f.read()

# Análise sintática
resultado = parser.parse(data, lexer=lexer)

print("\nÁrvore Sintática:\n")
print(resultado)
