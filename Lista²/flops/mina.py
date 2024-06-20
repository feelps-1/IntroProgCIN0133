tipoPicareta = input()

podeQuebrar = ["p", "a", "c"]
recursos = [0] * 5

if tipoPicareta != "basica":
    podeQuebrar.append("f")

if tipoPicareta == "ferro":
    podeQuebrar.append("o")

tamanhoMochila = input()

if tamanhoMochila == 'basica':
    tamanhoMochila = 10
elif tamanhoMochila == 'media':
    tamanhoMochila = 20
else:
    tamanhoMochila = 30

comida = [x for x in input().split(" - ")]
comida = [comida[0], int(comida[1]), int(comida[2])]

andares = int(input())
energia = 100
nDeBarris, itensBarril = 0, 0

terminou = False
andar = []
mochila = ["Picareta", comida[0]]
quantiaComida = comida[1]

if quantiaComida == 0:
    print("Vai ser tenso, vou levar nada pra repor minha energia...")
elif quantiaComida == 1:
    print(f"Hoje, irei levar apenas uma unidade de {comida[0]}.")
else:
    print(f"Bom estoque! vou levar {quantiaComida} unidades de {comida[0]}.")

if "nenhuma" in mochila:
    mochila.remove("nenhuma")

contagemAndar = 0

while not terminou:
    contagemAndar += 1
    tamanhoMatriz = [int(i) for i in input().split()]

    if tamanhoMatriz[0] == tamanhoMatriz[1]:
        print(f"Poxa! Esse andar é um quadrado perfeito de lado {tamanhoMatriz[0]}!!!")
    else:
        print(
            f"Esse andar da caverna parece um retângulo ou uma matriz {tamanhoMatriz[0]}x{tamanhoMatriz[1]}. Depois de minerar, ela ficou assim:")

    for i in range(tamanhoMatriz[0]):
        andar.append(input().split())

    for j in range(len(andar)):
        for k in range(len(andar[j])):
            if andar[j][k] == "b" or andar[j][k] in podeQuebrar:
                energia -= 3
                if andar[j][k] == "b":
                    nDeBarris += 1
                else:
                    recursos[podeQuebrar.index(andar[j][k])] += 1
                    if andar[j][k] not in mochila:
                        mochila.append(andar[j][k])
                andar[j][k] = "*"

    for i in andar:
        print(" ".join(i))

    for i in range(nDeBarris):
        barril = [b for b in input().split(", ")]
        if "rubi" in barril:
            if "rubi" not in mochila:
                print("MEU DEUS EU ACHEI UM RUBI NESSE BARRIL!!!")
                mochila.append("rubi")
        else:
            for j in barril:
                if j not in mochila:
                    mochila.append(j)

            print(f'Opa, quebrei o {i+1}º barril e recebi {len(barril)} itens.')

    andar = []
    nDeBarris = 0

    while energia <= 10 and quantiaComida > 0:
        energia += comida[2]
        quantiaComida -= 1
        if quantiaComida == 0:
            mochila.remove(comida[0])

    if contagemAndar == andares:
        terminou = True
        print("Cheguei aonde eu queria por hoje, vou sair.")
    elif energia < 10:
        terminou = True
        print(f"To sem energia para continuar minerando. Pelo menos cheguei ao andar {contagemAndar}.")
    else:
        print("Ainda dá pra continuar minerando, vamos simbora!!!")


print(f"""Pronto, acabei de sair da mina. Vamos ver o que eu consegui:
Total de pedra: {recursos[0]}.
Total de carvão: {recursos[1]}.
Total de cobre: {recursos[2]}.
Total de ferro: {recursos[3]}.
Total de ouro: {recursos[4]}.""")

if len(mochila) >= tamanhoMochila:
    print("A bolsa volta cheia hoje :)")

if "rubi" in mochila:
    print("A mineração hoje foi incrível!!!")
else:
    print("A mineração foi boa, mas ainda estão falando que roubei os melões :(")
