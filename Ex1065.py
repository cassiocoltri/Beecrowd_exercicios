"""
Faça um programa que leia 5 valores inteiros.
Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Ex Entrada:
7
-5
6
-4
12

3 valores pares
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

num = [n1, n2, n3, n4, n5]

cont = 0

for i in num:
    if i % 2 == 0:
        cont += 1

print(f"{cont} valores pares")
