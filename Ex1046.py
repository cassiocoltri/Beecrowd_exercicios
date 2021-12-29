"""
Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e
terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

Ex entrada:
1) 16 2
2) 2 16

Saída:
R1) O JOGO DUROU 10 HORA(S)
R2) O JOGO DUROU 14 HORA(S)
"""

hora_inicial, hora_final = input().split(" ")
hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

if hora_inicial > hora_final:
    total_jogo = (24 - hora_inicial) + hora_final
    print(f"O JOGO DUROU {total_jogo} HORA(S)")

elif hora_inicial < hora_final:
    total_jogo = hora_final - hora_inicial
    print(f"O JOGO DUROU {total_jogo} HORA(S)")

elif hora_inicial == hora_final:
    total_jogo = 24
    print(f"O JOGO DUROU {total_jogo} HORA(S)")
