"""
Escreva um programa que leia um valor inteiro N (1 < N < 1000).
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Ex: Entrada:
5

Saída:
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
"""
import math

x = int(input())
j = 1
for i in range(x):
    print(f"{j} {int(math.pow(j, 2))} {int(math.pow(j, 3))}")
    j += 1
