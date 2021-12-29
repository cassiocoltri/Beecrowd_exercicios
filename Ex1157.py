"""
Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.

Ex Entrada:
6

Saída:
1
2
3
6
"""

n1 = int(input())

for i in range(1, n1+1):
    if n1 % i == 0:
        print(i)
