suspeitos = []
locais = ["Torre do Mago", "Rancho da Marnie", "Saloon",
          "Armazém do Pierre", "Casa do Prefeito", "Peixaria",
          "Museu", "Ferreiro", "Mercado Joja",
          "Carpintaria", "Minas", "Centro Comunitário"]

for i in range(6):
    suspeitos.append([x for x in input().split(" - ")])

for i in suspeitos:
    i[1] = i[1].split(":")


