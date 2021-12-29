"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos.
A próxima linha deve mostrar a média dos valores positivos digitados.

Ex Entrada:
7
-5
6
-3.4
4.6
12

Saída:
4 valores positivos
7.4
"""

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

num = [n1, n2, n3, n4, n5, n6]

cont = 0
soma_positivo = 0

for i in num:
    if i > 0:
        cont += 1
        soma_positivo = soma_positivo + i

media = soma_positivo / cont
print(f"{cont} valores positivos")
print(f"{media:.1f}")
