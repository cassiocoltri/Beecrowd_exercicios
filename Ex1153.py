"""
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N

Ex entrada:  |  Saída:
4            | 24
"""

x = int(input())

fat = 1

for i in range(x, 0, -1):
    fat = fat * i
print(fat)
