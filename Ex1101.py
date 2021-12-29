"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos
entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N.
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Ex Entrada:    Saída:
5 2          | 2 3 4 5 Sum=14
6 3          | 3 4 5 6 Sum=18
5 0
"""

# x, y = input().split(" ")

while True:
    x, y = input().split(" ")
    soma = 0
    x = int(x)
    y = int(y)

    if x <= 0 or y <= 0:
        break

    if x > y:
        x, y = y, x
    for i in range(x, y + 1):
        soma += i
        print(f"{i} ", end="")
    print(f"Sum={soma}")

