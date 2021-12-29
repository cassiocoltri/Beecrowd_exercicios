"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence.
O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA
(nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida,
conforme o exemplo.

Entrada:   Sáida:
2 2    | primeiro -> X+ e Y +
3 -2   | quarto ->
-8 -1  | terceiro -> X- e Y-
-7 1   | segundo -> X+ e Y-
0 2    |
"""

while True:
    x, y = input().split(" ")

    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        print("primeiro")
    elif x > 0 and y < 0:
        print("quarto")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        print("segundo")
