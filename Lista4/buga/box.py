def criar_box():
    box = []
    for b in range(5):
        linha = []
        for j in range(6):
            linha.append(0)
        box.append(linha)

    return box


def capturar(computador, qnt):
    pcalterado = computador
    tamanho = len(pcalterado)

    while qnt > 0:
        for box in pcalterado:
            tamanho -= 1
            for linha in range(len(box)):
                for coluna in range(len(box[linha])):
                    if box[linha][coluna] == 0 and qnt != 0:
                        box[linha][coluna] = 1
                        qnt -= 1

        if qnt > 0:
            pcalterado.append(criar_box())

    return pcalterado


def transferir(computador, qnt):
    pcalterado = computador
    tamanho = len(pcalterado)

    while qnt > 0:
        for box in range(tamanho - 1, -1, -1):
            for linha in range(len(pcalterado[box]) - 1, -1, -1):
                for coluna in range(len(pcalterado[box][linha]) - 1, -1, -1):
                    if pcalterado[box][linha][coluna] == 1 and qnt != 0:
                        pcalterado[box][linha][coluna] = 0
                        qnt -= 1

                    if pcalterado[box][0][0] == 0 and box != 0:
                        pcalterado.pop()

                    if pcalterado[0][0][0] == 0:
                        qnt = 0

    return pcalterado


def mostrar_box(boxes):
    cnt = 1
    for box in boxes:
        for c in box:
            linhaprint = [' '.join(str(itens) for itens in x) for x in box]
            for j in linhaprint:
                matrizprint = '\n'.join(linhaprint)

        print(f"BOX {cnt}:")
        print(matrizprint)
        print()
        cnt += 1


armazenadosInicial = int(input())

if armazenadosInicial < 30:
    nBoxIniciais = 1
else:
    nBoxIniciais = armazenadosInicial // 30

pc = []

for i in range(nBoxIniciais):
    pc.append(criar_box())

pc = capturar(pc, armazenadosInicial)
pokemons = armazenadosInicial

acabou = False

while not acabou:
    comando = input()

    if comando == 'Capturar':
        quantidade = int(input())
        pc = capturar(pc, quantidade)
        pokemons += quantidade
        mostrar_box(pc)

    elif comando == 'Transferir':
        quantidade = int(input())
        pc = transferir(pc, quantidade)
        pokemons -= quantidade
        if pokemons < 0:
            pokemons = 0
        mostrar_box(pc)

    elif comando == 'Finalizar':
        acabou = True
        print("RELATÓRIO FINAL:")
        print()
        print(f"BOXES: {len(pc)}")
        print(f"POKEMONS: {pokemons}")
