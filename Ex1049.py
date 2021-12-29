"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo,
da esquerda para a direita.

Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

               /carnivoro -> aguia
           /ave
          /     \onivoro -> pomba

vertebrado         /onivoro -> homem
          \mamifero
                   \ herbivoro -> vaca

                    /hematofago -> pulga
            /inseto
invertebrado        \herbivoro -> lagarta
           \
            \        /hematofago -> sanguessuga
             anelideo
                     \onivoro -> minhoca

Ex Entrada:
vertebrado
mamifero
onivoro

Saída:
homem

"""

p1 = input()
p2 = input()
p3 = input()

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            print("aguia")

        elif p3 == "onivoro":
            print("pomba")

    elif p2 == "mamifero":
        if p3 == "onivoro":
            print("homem")

        elif p3 == "herbivoro":
            print("vaca")

elif p1 == "invertebrado":
    if p2 == "inseto":
        if p3 == "hematofago":
            print("pulga")

        elif p3 == "herbivoro":
            print("lagarta")

    elif p2 == "anelideo":
        if p3 == "hematofago":
            print("sanguessuga")

        elif p3 == "onivoro":
            print("minhoca")
