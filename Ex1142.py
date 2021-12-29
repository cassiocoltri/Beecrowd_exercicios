"""
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão
apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido

Ex Entrada:  | Saída:
7               1 2 3 PUM
                5 6 7 PUM
                9 10 11 PUM
                13 14 15 PUM
                17 18 19 PUM
                21 22 23 PUM
                25 26 27 PUM
"""

x = int(input())
j = 1
for i in range(x):
    print(f"{j} {j + 1} {j + 2} PUM")
    j += 4
