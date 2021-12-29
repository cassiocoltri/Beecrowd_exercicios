"""
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo
resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Ex Entrada: | Saída:
10         | 12
18         | 13
           | 17
"""

n1 = input()
n2 = input()

n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    n1, n2 = n2, n1

for i in range(n1, n2):
    if n1 < 0 or n2 < 0:
        break
    if i % 5 == 2 or i % 5 == 3:
        print(i)
