"""
Leia 5 valores Inteiros.
A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram positivos e
quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha,
não esquecendo o final de linha após cada uma.

Ex Entrada:
-5
0
-3
-4
12

Saida:
3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

num = [n1, n2, n3, n4, n5]

par = 0
impar = 0
posi = 0
nega = 0

for i in num:
    if i % 2 == 0:
        par += 1
        if i >= 0:
            posi += 1
        else:
            nega += 1
    else:
        impar += 1
        if i <= 0:
            nega += 1
        else:
            posi += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{posi} valor(es) positivo(s)")
print(f"{nega} valor(es) negativo(s)")
