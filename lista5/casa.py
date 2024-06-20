def percorrerLista(pasta):
    soma = 0
    for c in range(len(pasta)):
        if isinstance(pasta[c], list):
            resultado = percorrerLista(pasta[c])
            print(f'{resultado} -> {pasta[c]}')
            soma += resultado
        else:
            soma += pasta[c]

    return soma
    

pastas = eval(input())
print(f'{percorrerLista(pastas)} -> {pastas}')
