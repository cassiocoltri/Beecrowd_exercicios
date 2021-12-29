"""
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100),
indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um
valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação
fornecida.

Ex Entrada: / Saída:
3         |
8         | 8 nao eh primo
51        | 5 nao eh primo
7         | 7 eh primo
"""

test = int(input())

for i in range(test):

    x = int(input())
    ctt = 0

    for j in range(1, x):
        if x % j == 0:
            ctt += 1

    if ctt == 1:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
