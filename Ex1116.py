"""
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y)
que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel”
caso não seja possível efetuar o cálculo.


Entrada:   Sáida:
3       | -1.5
3 -2    | divisao impossivel
-8 0    | 0.0
0 8     |
"""

n = int(input())

for i in range(n):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if y == 0:
        print("divisao impossivel")
    else:
        div = float(x / y)
        print(f"{div:.1f}")
