"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Ex Entrada:
576

Saída:
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""

valor = int(input())
resto = 0

n100 = valor // 100
rest100 = valor % 100

n50 = rest100 // 50
rest50 = rest100 % 50

n20 = rest50 // 20
rest20 = rest50 % 20

n10 = rest20 // 10
rest10 = rest20 % 10

n5 = rest10 // 5
rest5 = rest10 % 5

n2 = rest5 // 2
rest2 = rest5 % 2

n1 = rest2 // 1

print(valor)
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")
