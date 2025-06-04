# Elgol Compiler

Este projeto é um analisador léxico e sintático para a linguagem Elgol, criado com as ferramentas PLY (Python Lex-Yacc).

O objetivo é reconhecer tokens e estruturas sintáticas da linguagem, além de identificar erros léxicos e sintáticos de forma clara.

## Estrutura

- `lexer/`: contém o analisador léxico (elgol_lexer.py)
- `parser/`: conterá o analisador sintático (elgol_parser.py)
- `tests/`: arquivos de teste para validar os analisadores

## Requisitos

- Python 3.13+
- ply

## Execução dos testes

```bash
python -m lexer.tests.test_lexer
