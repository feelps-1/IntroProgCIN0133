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

vida = int(input())
dano = 0
c = 0
acao = [
    [1, 3], [2, None], 
    [1, 3], [2, None],
    [1, 2], [2, 3],
    [1, None], [2, 1],
    [1, 1], [2, 2],
    [1, 1], [2, 2],
    [1, 1], [2, 2],
    [1, 1], [2, 2],
    [1, 1], [2, 2],
    [1, 1], [2, 2]
]

danos = [[9, 5, 10, 16, 20], [4, 9, 24, 20]]

for x in acao:
    print(f'x[1]: {x[1]}')

    if x[1] is None:
        c += 1
        print(f'C: {c}')
    else:
        print(f'Primo: {calcularPrimo(x[1])}')
        print(f'Vida % Primo: {vida % calcularPrimo(x[1])}')

        if vida % calcularPrimo(x[1]) == 0:
            dano += danos[x[0] - 1][x[1] - 1]
            print(f'Dano: {dano}')
            c += 1
            print(f'C: {c}')
        else:
            c += 1
            print(f'C: {c}')

    if c == 2:
        vida -= dano
        print(f'Vida: {vida}')
        c = 0
        print(f'C: {c}')
        dano = 0


'''
3
Filipe 2
89 3
Madu 10
38 88 39 97 4 11 86 19 34 32
Fernanda 5
64 37 7 6 79
638
['Filipe', 1], ['Madu', 5], ['Fernanda', None],
['Filipe', None], ['Madu', 3], ['Fernanda', None],
['Filipe', 1], ['Madu', 5], ['Fernanda', None],
['Filipe', None], ['Madu', 4], ['Fernanda', None],
['Filipe', None], ['Madu', 1], ['Fernanda', None],
['Filipe', 1], ['Madu', None], ['Fernanda', None],
['Filipe', 2], ['Madu', None], ['Fernanda', 4],
['Filipe', 1], ['Madu', 2], ['Fernanda', 3]
'''
