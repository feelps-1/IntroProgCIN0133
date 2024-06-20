def calcular_cp(atq, dfn, stm, multi):
    cp = (atq * (dfn ** 0.5) * (stm**0.5) * (multi ** 2)) / 10

    return cp


def desempate_cp(pokemons):
    maxcp = 0
    boss = ""
    for i in pokemons[1]:
        if i > maxcp:
            maxcp = i

    if pokemons[1].count(maxcp) > 1:
        for j in pokemons[1]:
            if j == maxcp:
                if len(pokemons[0][pokemons[1].index(j)]) > len(boss):
                    boss = pokemons[0][pokemons[1].index(j)]
        print(f"Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {boss}, com CP máximo de {maxcp:.2f}")
    else:
        boss = pokemons[0][pokemons[1].index(maxcp)]
        print(f"O Pokémon com o maior CP na região de Kanto é: {boss}, com CP máximo de {maxcp:.2f}")




terminou = False
analisados = [[], []]

while not terminou:
    nomePokemon = input()

    if nomePokemon == "Fim":
        terminou = True
    else:
        if nomePokemon not in analisados[0]:
            ataque = int(input())
            defesa = int(input())
            stamina = int(input())
            mult = float(input())

            analisados[0].append(nomePokemon)
            analisados[1].append(calcular_cp(ataque, defesa, stamina, mult))
            print("Pokémon computado com sucesso.")
        else:
            print("Opa, esse Pokémon já foi analisado.")


desempate_cp(analisados)
