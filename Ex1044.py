"""
Leia 2 valores inteiros (A e B).
Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

Ex Entrada:
1) 6 24
2) 6 25

Saída:
R1) Sao Multiplos
R2) Nao sao Multiplos
"""

a, b = input().split(" ")
a = int(a)
b = int(b)

if a < b:
    troca = a
    a = b
    b = troca

if (a/b) % 2 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
