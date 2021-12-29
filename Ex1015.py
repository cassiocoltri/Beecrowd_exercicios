"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula,
segundo a fórmula:
             ________________________
Distância = V(x2 - x1)² + (y2 - y1)²

Entrada:
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante:
x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída:
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

Ex Entrada:
1.0 7.0
5.0 9.0

Saída:
4.4721
"""
import math

x1, y1 = input().split(" ")
x2, y2 = input().split(" ")

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"{dist:.4f}")