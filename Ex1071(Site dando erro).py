"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro.
Este valor é a soma dos valores ímpares que estão entre
os valores fornecidos na entrada que deverá caber em um inteiro.

Ex Entrada:
1) 6, -5 (-5, -3, -1, 1, 3, 5) = 0?

2) 15, 12

Saída:
1) 5

2) 13
"""

n1 = int(input())
n2 = int(input())

cont = 0

if n1 < n2:
    n1, n2 = n2, n1

for i in range(n1, n2):
    if i % 2 != 0:
        cont += i

print(cont)
