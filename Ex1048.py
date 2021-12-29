"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

    Salário	       |   Percentual de Reajuste
000.00 - 400.00         -> 15%
400.01 - 800.00         -> 12%
800.01 - 1200.00        -> 10%
1200.01 - 2000.00        -> 7%
Acima de 2000.00         -> 4%

Leia o salário do funcionário e calcule e mostre o novo salário,
bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho,
conforme exemplo abaixo.

Ex Entrada:
400.00

Sáida:
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %
"""

salario = float(input())

if 0.00 < salario <= 400.00:
    perc = 15
    novo_salario = salario + (salario / 100 * perc)
    reajuste = novo_salario - salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {perc} %")

elif 400.01 <= salario <= 800.00:
    perc = 12
    novo_salario = salario + (salario / 100 * perc)
    reajuste = novo_salario - salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {perc} %")

elif 800.01 <= salario <= 1200.00:
    perc = 10
    novo_salario = salario + (salario / 100 * perc)
    reajuste = novo_salario - salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {perc} %")

elif 1200.01 <= salario <= 2000.00:
    perc = 7
    novo_salario = salario + (salario / 100 * perc)
    reajuste = novo_salario - salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {perc} %")
else:
    perc = 4
    novo_salario = salario + (salario / 100 * perc)
    reajuste = novo_salario - salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {perc} %")
