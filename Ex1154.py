"""
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo.
O último dado, que não entrará nos cálculos, contém o valor de idade negativa.
Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.

Ex entrada:  |  Saída:
34           | 39.25
56
44
23
-2
"""

ctt = 0
somaIdades = 0

while True:
    x = int(input())

    if x < 0:
        media = float(somaIdades / ctt)
        break
    else:
        ctt += 1
        somaIdades += x
print(f"{media:.2f}")
