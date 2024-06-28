'''
def buscaArmas(vida, dadosContas, buscadas=[[] for c in range(len(nomes))]):
    acao = [[], []]
    for c in range(len(dadosContas[0])):
        primo = False
        for d in range(len(1, dadosContas[1][c] + 1)):
            num = d

            while not primo:
                divisiveis = 0
                for e in range(1, num + 1):
                    if num % e == 0:
                        divisiveis += 1

                    if divisiveis > 2:
                        primo = True
                        break

                num += 1
                
            if vida % num == 0 and d not in acao[1]:
                acao[0].append(dadosContas[0][c])
                acao[1].append(d)
                vida -= dadosContas[2][c][d]
                break
        
        for c in range(acao[1]):
            buscadas[c].append(acao[1][c])
            

2
Anne 5
52 5 18 57 69
Walter 7
66 90 48 15 63 14 93
187
'''

def calcularPrimo(numero):
    primos = 0
    num = 0

    while not primos == numero:
        num += 1
        divisiveis = 0
        for e in range(1, num + 1):
            if num % e == 0: divisiveis += 1

            if divisiveis > 2:
                break

        if divisiveis == 2: primos += 1

    return num

def buscaArmas(vida, dadosContas, acao=[], alvo=0, usadas=[], turno=0):
    if vida <= 0:
        acao.append(True)
        return acao

    for d in range(1, dadosContas[1][alvo] + 1):
        if len(acao) > 0 and acao[-1][0] == dadosContas[0][alvo]: acao.pop()

        if len(acao) > 0 and acao[-1] != True:
            usadas = []
            armas = [x[1] for x in acao[turno * len(dadosContas[0]):]]
            for x in armas:
                if x != None:
                    usadas.append(x)
                
        print('\n\n', acao)
        print(f'Alvo: {alvo} - D: {d} - Usadas: {usadas} - Turno: {turno} - Vida: {vida}\n\n')
        if len(acao) > 0 and acao[-1] == True: return acao

        num = calcularPrimo(d)

        if vida % num == 0 and d not in usadas:
            acao.append([dadosContas[0][alvo], d])
            if alvo < len(dadosContas[0]) - 1:
                acao = buscaArmas(vida, dadosContas, acao, alvo + 1, usadas, turno)
            elif alvo == len(dadosContas[0]) - 1:
                for c in range(len(acao) - turno * len(dadosContas[0])):
                    if acao[c + turno * len(dadosContas[0])][1] != None:
                        if dadosContas[2][c][acao[c + turno * len(dadosContas[0])][1] - 1] != None: vida -= dadosContas[2][c][acao[c + turno * len(dadosContas[0])][1] - 1]
                
                if vida <= 0:
                    acao.append(True) 
                    return acao
                else:
                    acao = buscaArmas(vida, dadosContas, acao, turno=turno + 1)
        elif d == dadosContas[1][alvo]:
            acao.append([dadosContas[0][alvo], None])
            if alvo == len(dadosContas[0]) - 1:
                none = 0
                for c in range(turno * len(dadosContas[0]), len(acao)):
                    if acao[c][1] == None:
                        none += 1
                
                if none >= len(dadosContas[0]):
                    acao[-len(dadosContas[0]):] = [[False, 1]]
                    return acao

                for c in range(len(acao) - turno * len(dadosContas[0])):
                    if acao[c + turno * len(dadosContas[0])][1] != None:
                        vida -= dadosContas[2][c][acao[c + turno * len(dadosContas[0])][1] - 1]
                
                if vida <= 0:
                    acao.append(True) 
                    return acao
                else:
                    acao = buscaArmas(vida= vida, dadosContas=dadosContas, acao=acao, turno=turno + 1, usadas=[])
            else:
                acao = buscaArmas(vida, dadosContas, acao, alvo + 1, usadas, turno)

    if len(acao) > 0 and acao[-1][0] == False:
        if acao[-1][1] >= len(dadosContas[0]):
            acao.pop()
        else:
            acao[-1][1] += 1

    if vida > 0 and len(acao) > 0 and acao[-1][0] != False:
        acao.pop()

    return acao
        


qtContas = int(input())

dadosContas = [[], [], []] 

for c in range(qtContas):
    nome, qtArmas = input().split()
    danoArmas = input()
    dadosContas[0].append(nome)
    dadosContas[1].append(int(qtArmas))
    dadosContas[2].append([int(dano) for dano in danoArmas.split()])

print(dadosContas)
vidaInimigo = int(input())
print(buscaArmas(vidaInimigo, dadosContas))

'''
Case: 1

Input

2
Anne 5
52 5 18 57 69
Walter 7
66 90 48 15 63 14 93
187

Output

Felizmente conseguimos vencer!
A seguinte sequencia de acoes pode ser usada:
Anne arma_5 arma_3 arma_4
Walter arma_7 nada nada

Case: 2

Input

3
Filipe 2
89 3
Madu 10
38 88 39 97 4 11 86 19 34 32
Fernanda 5
64 37 7 6 79
638

Output

Felizmente conseguimos vencer!
A seguinte sequencia de acoes pode ser usada:
Filipe arma_1 nada arma_1 arma_1 arma_1 arma_1
Madu arma_5 arma_3 arma_9 arma_8 arma_4 nada
Fernanda nada nada arma_5 nada nada nada

Case: 3

Input

2
Francisco 5
9 5 10 16 20
Sergio 4
4 9 24 20
155

Output

Infelizmente nao conseguiremos vencer dessa vez.
'''