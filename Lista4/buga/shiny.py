def registrar(n):
    info = [[],
            [],
            [],
            []]

    for i in range(n):
        apresenta = input()
        apresenta = apresenta.split()

        nome = apresenta[4].strip(",")
        favorito = apresenta[9]
        pokebolas = int(apresenta[12])

        info[0].append(nome)
        info[1].append(favorito)
        info[2].append(pokebolas)
        info[3].append([])

    return info


def cifra_jogadores(jogador):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    cifrado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    nomecifrado = ""

    for i in range(3):
        cifrado.append(cifrado.pop(0))

    for i in jogador:
        nomecifrado += cifrado[alfabeto.index(i.lower())]

    idn = 0

    for j in nomecifrado:
        idn += ord(j)

    return str(idn)[-1]


def cifra_pokemon(criatura, passos, segundos):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    cifrado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(passos):
        cifrado.append(cifrado.pop(0))

    nomecifrado = ""

    for i in criatura:
        nomecifrado += cifrado[alfabeto.index(i.lower())]

    idn = 0

    for j in nomecifrado:
        idn += ord(j)

    idn = idn * segundos

    return str(idn)[-1]


def encontros():
    treinadores = registrar(int(input()))
    encontroufavorito = False

    while not encontroufavorito:
        encontro = input()
        encontro = encontro.split()

        pokemon = encontro[1]
        tempo = int(encontro[5])
        passos = int(encontro[8])
        participante = encontro[-1]

        pokebolas = treinadores[2][treinadores[0].index(participante)]

        favorito = treinadores[1][treinadores[0].index(participante)]

        bag = treinadores[3][treinadores[0].index(participante)]

        idtreinador = cifra_jogadores(participante)
        idpokemon = cifra_pokemon(pokemon, passos, tempo)

        if pokemon == favorito and idtreinador == idpokemon and pokebolas == 1:
            print(f"{participante}: Que sorte! Não apenas achei meu shiny favorito, como também o capturei em minha última pokébola!!!")
            bag.append(pokemon)
            encontroufavorito = True
        elif pokemon == favorito and idtreinador == idpokemon and pokebolas > 1:
            print(f"{participante}: Consegui capturar um {favorito} shiny!")
            bag.append(pokemon)
            treinadores[2][treinadores[0].index(participante)] -= 1
            encontroufavorito = True
        elif idpokemon == idtreinador and pokemon in bag and pokebolas >=1:
            print(f"{participante}: Achei um {pokemon} shiny, mas não posso desperdiçar pokébolas em um shiny que já tenho...")
        elif idpokemon == idtreinador and pokemon != favorito and pokebolas >= 1:
            print(f"{participante}: Mais um shiny para a coleção, mas ainda não é um {favorito}")
            bag.append(pokemon)
            treinadores[2][treinadores[0].index(participante)] -= 1
        elif pokemon == favorito and pokebolas >= 1:
            print(f"{participante}: Uau, um {favorito}! Pena que não é um shiny...")
            treinadores[2][treinadores[0].index(participante)] -= 1
        elif idpokemon == idtreinador and pokemon == favorito and pokebolas < 1:
            print(f"{participante}: Só pode ser brincadeira, um {favorito} shiny logo agora?!")
        elif idtreinador == idpokemon and pokebolas < 1:
            print(f"{participante}: Péssimo momento, encontrei um {pokemon} shiny, mas não tenho mais pokébolas!")
        elif pokemon == favorito and pokebolas < 1:
            print(f"{participante}: Desculpa, meu querido {favorito}, mas não poderei lhe capturar hoje")
        elif pokebolas < 1:
            print(f"{participante}: Só um {pokemon} normal?Bom, não é como se eu tivesse pokébolas para capturar algo raro mesmo...")
        else:
            print(f"{participante}: Ainda não é um {favorito} shiny, tenho que continuar procurando...")

    print()
    print("---Vamos verificar o que todos encontraram!---")
    for j in range(len(treinadores[3])):
        if not treinadores[3][j]:
            print(f"Coitado, {treinadores[0][j]} não conseguiu capturar um único shiny hoje")
        else:
            shinies = ", ".join(treinadores[3][j])
            print(f"{treinadores[0][j]} capturou os seguintes shinies: {shinies}")

encontros()