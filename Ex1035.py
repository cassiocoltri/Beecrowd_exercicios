"""
Leia 4 valores inteiros A, B, C e D. (ok)
A seguir:
Se B for maior do que C e se D for maior do que A, (ok)
e a soma de C com D for maior que a soma de A e B (ok)
e se C e D, ambos, forem positivos (ok)
e se a variável A for par escrever a mensagem "Valores aceitos",
senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

Ex Entrada:
5 6 7 8

Saída:
Valores nao aceitos
"""

a, b, c, d = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

soma_CD = c + d
soma_AB = a + b

if b > c and d > a and soma_CD > soma_AB and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
