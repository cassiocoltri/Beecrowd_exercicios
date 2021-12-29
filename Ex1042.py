"""
Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida,
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Ex Entrada:
7 21 -14

Saída:
-14
7
21

7
21
-14
"""

n1, n2, n3 = input().split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

valor = [n1, n2, n3]

valor.sort()

print(valor[0])
print(valor[1])
print(valor[2])
print()
print(n1)
print(n2)
print(n3)
