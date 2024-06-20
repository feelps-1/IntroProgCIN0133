qnt = int(input())

nomes = [i for i in input().split()]
irrita = [i for i in input().split()]

saida = []
passou = []

for i in range(qnt):
    for j in irrita:
        if j not in passou or j == nomes[i]:
            saida.append(j)
            break

    if nomes[i] not in passou:
        passou.append(nomes[i])

pipi = " ".join(saida)

print(f"{pipi}\n")