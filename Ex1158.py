"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. (check)
Cada caso de teste consiste de dois inteiros X e Y. (check)

Você deve apresentar a soma de Y ímpares consecutivos a partir de X
inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.

Ex Entrada: |  Saída:
2           |
4 3         | (5 + 7 + 9) = 21
11 2        | (11 + 13) = 24
"""

n1 = int(input())

for i in range(n1):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)

    if x % 2 == 0:
        x = (x + 1)

    soma = 0

    for j in range(y):
        soma += x
        x = (x + 2)

    print(soma)
