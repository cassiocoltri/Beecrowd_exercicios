"""
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1.
Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

Ex Entrada: / Saída:
0         | X[0] = 1
-5        | X[1] = 1
63        | X[2] = 63
0         | X[3] = 1
...       | ...
"""

x = []

for i in range(10):
    x.append(int(input()))

novaList = [int(val) for val in x]

for k in range(len(novaList)):
    if novaList[k] <= 0:
        novaList[k] = 1

for j in range(len(novaList)):
    print(f"X[{j}] = {novaList[j]}")
