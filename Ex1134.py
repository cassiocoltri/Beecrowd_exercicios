"""
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4)
deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código
informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível,
conforme exemplo.

Ex Entrada:  | Saída: MUITO OBRIGADO
8               Alcool: 1
1               Gasolina: 2
7               Diesel: 0
2
2
4
"""

gas, die, alc, x = 0, 0, 0, 0

while x != 4:
    x = int(input())
    if x == 1:
        alc += 1
    elif x == 2:
        gas += 1
    elif x == 3:
        die += 1
    elif x == 4:
        break
    else:
        continue

print("MUITO OBRIGADO")
print(f"Alcool: {alc}")
print(f"Gasolina: {gas}")
print(f"Diesel: {die}")
