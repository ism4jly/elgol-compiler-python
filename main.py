from lexer.elgol_lexer import lexer

with open("examples/exemplo1.elgol", encoding="utf-8") as f:
    data = f.read()

lexer.input(data)

print("Tokens encontrados:\n")
for token in lexer:
    print(f"{token.type:<15} -> {token.value}")
