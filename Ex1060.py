"""
Faça um programa que leia 6 valores.
Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Ex Entrada:
7
-5
6
-3.4
4.6
12

Saida:
4 valores positivos

"""

num = []
cont = 0

while len(num) < 6:
    i = float(input())
    if i > 0:
        cont += 1
    num.append(i)

print(f"{cont} valores positivos")
