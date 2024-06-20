def pokemon(poke):
    dados = []
    nome, tipo, nivel, vida, poder, defesa, velocidade, nomeataque, atkpwr = poke.split(", ")

    nivel = int(nivel)
    vida, vidamax = int(vida), int(vida)
    poder = int(poder)
    defesa = int(defesa)
    velocidade = int(velocidade)
    atkpwr = int(atkpwr)

    dados = [nome, tipo, nivel, vida, poder, defesa, velocidade, nomeataque, atkpwr, vidamax]

    return dados


def efetividade(tipo_atacante, tipo_defesa):
    multEfetivo = 0

    if tipo_atacante == "fogo":
        if tipo_defesa == "grama":
            multEfetivo = 2
            return multEfetivo
        elif tipo_defesa == "água":
            multEfetivo = 0.5
            return multEfetivo
        else:
            multEfetivo = 1
            return multEfetivo
    elif tipo_atacante == "agua":
        if tipo_defesa == "grama":
            multEfetivo = 0.5
            return multEfetivo
        elif tipo_defesa == "fogo":
            multEfetivo = 0.5
            return multEfetivo
        else:
            multEfetivo = 1
            return multEfetivo
    elif tipo_atacante == "grama":
        if tipo_defesa == "fogo":
            multEfetivo = 0.5
            return multEfetivo
        elif tipo_defesa == "agua":
            multEfetivo = 2
            return multEfetivo
        else:
            multEfetivo = 1
            return multEfetivo
    else:
        multEfetivo = 1
        return multEfetivo


def calculo_dano(nivel, poder, defesainimigo, poderataque, efetivo):
    dano = 0

    dano = int((((((2 * nivel) + 10) / 250) * ((poder / defesainimigo) * poderataque)) + 2) * efetivo)

    return dano


inicial = pokemon(input())
print(f"escolho você {inicial[0]}")

acabou = False

while not acabou:
    encontro = input()
    equipeRocket = False

    if encontro == "um pokemon selvagem aparece!":
        print("vamo botar pra quebrar!")
    else:
        print(f"{inicial[0]}, bora acabar com a raça desses bandidos e salvar o professor!")
        equipeRocket = True

    print()

    pokemonInimigo = pokemon(input())

    vida = inicial[3]
    velocidadeInicial = inicial[6]
    efetividadeInicial = efetividade(inicial[1], pokemonInimigo[1])
    danoInicial = calculo_dano(inicial[2], inicial[4], pokemonInimigo[5], inicial[8], efetividadeInicial)

    vidaInimigo = pokemonInimigo[3]
    efetividadeInimigo = efetividade(pokemonInimigo[1], inicial[1])
    velocidadeInimigo = pokemonInimigo[6]
    danoInimigo = calculo_dano(pokemonInimigo[2], pokemonInimigo[4], inicial[5], pokemonInimigo[8], efetividadeInimigo)

    seuTurno = True

    if velocidadeInimigo > velocidadeInicial:
        seuTurno = False

    combate = True
    rodadaPlayer, rodadaInimigo = False, False
    comando = ""

    while combate:
        if not rodadaInimigo and not rodadaPlayer:
            comando = input()
        if comando == "correr" and equipeRocket:
            print("lascou, eles não largam do meu pé!")
        elif comando == "correr":
            print("ufa, consegui meter o pé!")
            combate = False
        else:
            if seuTurno:
                rodadaPlayer = True
                print(f"{inicial[0]} usou {inicial[7]}")
                if efetividadeInicial == 2:
                    print("foi super efetivo!")
                elif efetividadeInicial == 0.5:
                    print("não foi muito efetivo")
                vidaInimigo -= danoInicial
                if vidaInimigo < 0:
                    vidaInimigo = 0
                seuTurno = False

            elif not seuTurno:
                print(f"{pokemonInimigo[0]} usou {pokemonInimigo[7]}")
                rodadaInimigo = True
                if efetividadeInimigo == 2:
                    print("foi super efetivo!")
                elif efetividadeInimigo == 0.5:
                    print("não foi muito efetivo")
                vida -= danoInimigo
                if vida < 0:
                    vida = 0
                seuTurno = True

        if rodadaPlayer and rodadaInimigo:
            print(f"HP: {vida:.0f}/{inicial[-1]} | HP inimigo: {vidaInimigo:.0f}/{pokemonInimigo[-1]}")
            rodadaPlayer, rodadaInimigo = False, False

        inicial[3] = vida

        if equipeRocket and vidaInimigo == 0:
            print(f"HP: {vida:.0f}/{inicial[-1]} | HP inimigo: {vidaInimigo:.0f}/{pokemonInimigo[-1]}")
            print(f"{pokemonInimigo[0]} derrotado!")
            print()
            print(f"Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {inicial[0]}?")
            acabou = True
            combate = False
        elif vida == 0:
            print(f"HP: {vida:.0f}/{inicial[-1]} | HP inimigo: {vidaInimigo:.0f}/{pokemonInimigo[-1]}")
            print(f"{inicial[0]} derrotado!")
            print()
            print("Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.")
            acabou = True
            combate = False
        elif vidaInimigo == 0:
            print(f"HP: {vida:.0f}/{inicial[-1]} | HP inimigo: {vidaInimigo:.0f}/{pokemonInimigo[-1]}")
            combate = False
            print(f"{pokemonInimigo[0]} derrotado!")
            print()





