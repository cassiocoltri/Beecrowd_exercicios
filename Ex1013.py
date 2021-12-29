"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos
seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Ex Entrada:
7 14 106

Saída:
106 eh o maior
"""

n1, n2, n3 = input().split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print(f"{n1} eh o maior")
elif n2 > n3:
    print(f"{n2} eh o maior")
else:
    print(f"{n3} eh o maior")
