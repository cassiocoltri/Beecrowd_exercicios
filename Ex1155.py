"""
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 1/2 + 1/3 + … + 1/100

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.

"""

s = 0

for i in range(1, 100+1):
    s += float(1/(i+1))

total = (s + 1.0) - 0.01

print(f"{total:.2f}")
