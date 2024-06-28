'''
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

def buscaArmas(vida, dadosContas, acao=[], alvo=0, usadas=[], turno=0, qtNone=0):
    for c in range(dadosContas[1][alvo]):
        num = calcularPrimo(c + 1)
        

        if vida <= 0:
            return acao


        if vida % num == 0 and c not in usadas:
            input()
            if alvo < len(dadosContas[0]) - 1:
                print(f'NÂO É O ULTIMO Vida Atual: {vida}, Acao: {acao + [[dadosContas[0][alvo], c + 1]]}, Alvo: {alvo}, Usadas: {usadas}, Turno: {turno}, C: {c}, Num: {num}, Vida % Num: {vida % num}, Dano: {dadosContas[2][alvo][c]}, Vida - Dano: {vida - dadosContas[2][alvo][c]}')
                resultado = buscaArmas(vida, dadosContas, acao + [[dadosContas[0][alvo], c + 1]], alvo + 1, usadas + [c], turno, qtNone)
                if resultado is not None:
                    return resultado
            else:
                print(f'É O ULTIMO Vida Atual: {vida}, Acao: {acao + [[dadosContas[0][alvo], c + 1]]}, Alvo: {alvo}, Usadas: {usadas}, Turno: {turno}, C: {c}, Num: {num}, Vida % Num: {vida % num}, Dano: {dadosContas[2][alvo][c]}, Vida - Dano: {vida - dadosContas[2][alvo][c]}')
                input()
                acao.append([dadosContas[0][alvo], c + 1])
                for d in range(turno * len(dadosContas[0]), len(acao)):
                    if acao[d][1] != None:
                        vida -= dadosContas[2][dadosContas[0].index(acao[d][0])][acao[d][1] - 1]
                        print(f'Vida: {vida}, Dano: {dadosContas[2][dadosContas[0].index(acao[d][0])][acao[d][1] - 1]}')

                if vida <= 0:
                    return acao

                acao.pop(-1)
                resultado = buscaArmas(vida, dadosContas, acao + [[dadosContas[0][alvo], c + 1]], 0, [], turno + 1, 0)
                if resultado is not None:
                    return resultado

        print(dadosContas[1][alvo] - 1, c)
        if c == dadosContas[1][alvo] - 1:
            print(f'NONE Vida Atual: {vida}, Acao: {acao + [[dadosContas[0][alvo], None]]}, Alvo: {alvo}, Usadas: {usadas}, Turno: {turno}, C: {c}, Num: {num}, Vida % Num: {vida % num}, Dano: {dadosContas[2][alvo][c]}, Vida - Dano: {vida - dadosContas[2][alvo][c]}')
            input()
            if alvo < len(dadosContas[0]) - 1:
                resultado = buscaArmas(vida, dadosContas, acao + [[dadosContas[0][alvo], None]], alvo + 1, usadas, turno, qtNone + 1)
                if resultado is not None:
                    return resultado
            else:
                if qtNone + 1 == len(dadosContas[0]):
                    return None

                for d in range(turno * len(dadosContas[0]), len(acao)):
                    if acao[d][1] != None:
                        print(f'Vida: {vida}, Dano: {dadosContas[2][dadosContas[0].index(acao[d][0])][acao[d][1] - 1]}, Nova Vida: {vida - dadosContas[2][dadosContas[0].index(acao[d][0])][acao[d][1] - 1]}')
                        vida -= dadosContas[2][dadosContas[0].index(acao[d][0])][acao[d][1] - 1]

                if vida <= 0:
                    return acao

                resultado = buscaArmas(vida, dadosContas, acao + [[dadosContas[0][alvo], None]], 0, [], turno + 1, 0)
                if resultado is not None:
                    return resultado

    print('NONOU')
    return None


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