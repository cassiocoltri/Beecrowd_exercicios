"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

Ex Entrada:
None

Saída:
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
"""

# for i in range(1, 60, 3):
#     for j in range(60, 0, -5):
#         print(f"I={i} J={j}")

i = 1
j = 60

for x in range(1, 14):
    print(f"I={i} J={j}")
    i += 3
    j -= 5
