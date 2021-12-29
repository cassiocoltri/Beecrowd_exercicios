"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

Ex Entrada:
2
113
45
34565
6
...
8

Saída:
34565
4
"""

numeros = []

for i in range(100):
    numeros.append(int(input()))

posicao = numeros.index(max(numeros))

print(max(numeros))
print(posicao+1)
