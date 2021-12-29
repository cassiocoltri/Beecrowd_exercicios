"""
Leia um valor inteiro X.
Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

Ex Entrada:
8

Saida:
9
11
13
15
17
19
"""
numero = int(input())
cont = 0

for i in range(numero, numero * numero):
    if i % 2 != 0:
        print(i)
        cont += 1
        if cont == 6:
            break
