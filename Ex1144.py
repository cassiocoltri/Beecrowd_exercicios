"""
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa,
seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

Entrada
O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

Saída
Imprima a saída conforme o exemplo fornecido.

Ex Entrada: 5

Saída:
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
"""
import math

x = int(input())
j = 1
for i in range(x):
    print(f"{j} {int(math.pow(j, 2))} {int(math.pow(j, 3))}")
    print(f"{j} {int(math.pow(j, 2)+1)} {int(math.pow(j, 3)+1)}")
    j += 1
