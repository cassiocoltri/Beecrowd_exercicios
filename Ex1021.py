"""
Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário. A seguir, calcule o menor número de notas e
moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de:
100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial,
conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Ex Entrada:
576.73

Saída:

NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
"""

valor = float(input())

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

m_100 = rest2 // 1.0
rest_1 = rest2 % 1.0

m_050 = rest_1 // 0.50
rest_050 = rest_1 % 0.50

m_025 = rest_050 // 0.25
rest_025 = rest_050 % 0.25

m_010 = rest_025 // 0.10
rest_010 = rest_025 % 0.10

m_005 = rest_010 // 0.05
rest_m005 = rest_010 % 0.05

m_001 = rest_m005 / 0.01

print("NOTAS:")
print(f"{n100:.0f} nota(s) de R$ 100.00")
print(f"{n50:.0f} nota(s) de R$ 50.00")
print(f"{n20:.0f} nota(s) de R$ 20.00")
print(f"{n10:.0f} nota(s) de R$ 10.00")
print(f"{n5:.0f} nota(s) de R$ 5.00")
print(f"{n2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{m_100:.0f} moeda(s) de R$ 1.00")
print(f"{m_050:.0f} moeda(s) de R$ 0.50")
print(f"{m_025:.0f} moeda(s) de R$ 0.25")
print(f"{m_010:.0f} moeda(s) de R$ 0.10")
print(f"{m_005:.0f} moeda(s) de R$ 0.05")
print(f"{m_001:.0f} moeda(s) de R$ 0.01")
