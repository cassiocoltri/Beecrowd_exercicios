"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

Saída:
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""

for i in range(10):
    if i % 2 != 0:
        print(f"I={i} J=7")
        print(f"I={i} J=6")
        print(f"I={i} J=5")

