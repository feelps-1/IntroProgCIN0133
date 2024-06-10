import matplotlib.pyplot as plt

def fact(fator):
    fatorial = 1
    for j in range(1, fator+1):
        fatorial *= j

    return int(fatorial)


def pessoas(salas, pessoasqnt):
    saida = [[], []]
    qnt = 0

    for i in range(pessoasqnt + 1):

        pessoasfact = fact(pessoasqnt)

        qntfact = fact(qnt)

        m = fact(pessoasqnt - qnt)

        if qnt == 0 or qnt == 10:
            comb = 1
        else:
            comb = pessoasfact / (qntfact * m)

        resto = (salas - 1) ** (pessoasqnt - qnt)

        divisor = salas ** pessoasqnt

        probabilidade = (comb * resto) / divisor

        print(f"O número de maneiras de distribuir na sala é de {divisor} maneiras e a probabilidade de ter {qnt} pessoas na sala é de {comb}/{divisor} = {probabilidade:.6f}%")
        qnt += 1
        saida[0].append(qnt)
        saida[1].append(probabilidade)

    return saida


def quantas(qnt, ligacoes):
    temp = 0
    saida = [[], []]

    for i in range(qnt + 1):
        quantasFact = fact(qnt)
        tempFact = fact(temp)
        ligFact = fact(ligacoes)

        prob = (quantasFact**4)/(ligFact*((tempFact*fact(qnt-temp))**2))

        print(f"A probabildade do sólido A ter {temp} de temperatura com {ligacoes} ligações é de {prob:.6f}%")
        temp += 1
        saida[0].append(temp)
        saida[1].append(prob)

    return saida


def show_quantas(quantasn, ligacoesn):
    dados = quantas(quantasn, ligacoesn)

    eixox = dados[0]
    eixoy = dados[1]

    ticks = [j for j in range(len(eixox)+1)]

    labels = [""]

    for i in range(len(eixox)):
        labels.append(i)

    fig, ax = plt.subplots(figsize=(8.5, 6))
    bar_container = ax.bar(eixox, eixoy, color='blue')
    ax.set_xticks(ticks, labels)
    ax.set(ylabel="Probabilidade (%)", title="Distribução de quantas", xlabel="Temperatura", ylim=(0, 0.4))
    ax.bar_label(bar_container, fmt="{:,.5f}%")

    plt.show()


def show_pessoas(salasn, pessoasn):
    dados = pessoas(salasn, pessoasn)

    eixox = dados[0]
    eixoy = dados[1]

    ticks = [j for j in range(len(eixox) + 1)]

    labels = [""]

    for i in range(len(eixox)):
        labels.append(i)

    fig, ax = plt.subplots(figsize=(9, 6))
    bar_container = ax.bar(eixox, eixoy, color='green')
    ax.set_xticks(ticks, labels)
    ax.set(ylabel="Probabilidade (%)", title="Distribuição das pessoas", xlabel="Pessoas na sala")
    ax.bar_label(bar_container, fmt="{:,.5f}%")

    plt.show()


show_quantas(8, 16)

show_pessoas(2, 10)
