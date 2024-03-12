import random
import math

def simulaJogo(time1, time2):
    golsTotais = random.randrange(10)
    golsTime1 = math.trunc(golsTotais*((time1.ataque)/(time1.ataque+time2.ataque)))
    golsTime2 = math.trunc(golsTotais*((time2.ataque)/(time1.ataque+time2.ataque)))

    for i in range(golsTime1):
        time1.scoringChance(time2)
    
    for j in range(golsTime2):
        time2.scoringChance(time1)

    print(f'{time1.nome} {time1.gols} x {time2.gols} {time2.nome}')

    if time1.gols > time2.gols:
        return time1.nome
    elif time1.gols == time2.gols:
        return 'Empate'
    else:
        return time2.nome
    