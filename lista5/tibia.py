def buscaArmas(vida, nomes, armas, buscadas=[]):
    acoes = [[] for c in range(len(nomes))]
    acao = []
    for c in range(len(nomes)):
        for d in range(len(armas[c])):
            if vida % d == 0:
                acao.append(d)


qtContas = int(input())

dadosContas = [['', [], []] for c in range(qtContas)]

for c in range(qtContas):
    nome, qtArmas = input().split()
    danoArmas = input()
    dadosContas[c][0] = nome
    dadosContas[c][1] = qtArmas
    dadosContas[c][2] = danoArmas

vidaInimigo = int(input())


