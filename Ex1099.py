"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. (check)
Cada caso de teste consiste de dois inteiros X e Y. (check)
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

Ex Entrada:  |  Sáida:
7            |
4 5          | 0
13 10        | 11
6 4          | 5
3 3          | 0
3 5          | 0
3 4          | 0
3 8          | 12
"""

n = int(input())

for i in range(n):
    soma = 0
    x, y = input().split(" ")

    if x > y:
        x, y = y, x

    x = int(x)
    y = int(y)

    for j in range(x+1, y):
        if j % 2 != 0:
            soma += j

    print(soma)
