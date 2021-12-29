"""
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último,
o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

Ex Entrada: / Saída:
0           | N[0] = 230
-5          | N[1] = 63
...         | ...
63          | N[18] = -5
230         | N[19] = 0

"""
8
x = []

for i in range(20):
    x.append(input())

novaList = [int(val) for val in x]

novaList.reverse()

for j in range(len(novaList)):
    print(f"N[{j}] = {novaList[j]}")
