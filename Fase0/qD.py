from math import floor

info = [int(x) for x in input().split()]

ext = info[0]
velocidade = info[1]

horasTotal = ext / velocidade

if horasTotal > 24:
    horasTotal = horasTotal % 24

minutosTotal = round((horasTotal - floor(horasTotal)) * 60)

horaInicial = 19

horaFinal = int(horaInicial + horasTotal)

if horaFinal == 24:
    saidaHora = "00"
elif horaFinal > 24:
    horaFinal = horaFinal - 24
    if horaFinal < 10:
        saidaHora = "0" + str(horaFinal)
    else:
        saidaHora = str(horaFinal)
else:
    saidaHora = str(horaFinal)

if minutosTotal < 10:
    saidaMinutos = "0" + str(int(minutosTotal))
elif minutosTotal == 60:
    horaFinal = str(int(horaFinal) + 1)
    saidaMinutos = "00"
else:
    saidaMinutos = str(int(minutosTotal))

saida = saidaHora + ":" + saidaMinutos

print(saida)




