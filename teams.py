import random

class Team:
    def __init__(self, defesa, ataque, nome):
        self.defesa = defesa
        self.ataque = ataque
        self.gols = 0
        self.nome = nome

    def scoringChance(self, oponente):
        odds = self.ataque - oponente.defesa
        balanceador = random.randrange(20)
        odds = balanceador + odds

        if odds >= 15:
            self.gols += 1


Fluminense = Team(78,84, 'Fluminense')
Vasco = Team(75,79, 'Vasco')
Botafogo = Team(77,77, 'Botafogo')
Flamengo = Team(78,82, 'Flamengo')
Cruzeiro = Team(74,74, 'Cruzeiro')
Palmeiras = Team(80,84, 'Palmeiras')

times = [Fluminense, Vasco, Botafogo, Flamengo, Cruzeiro, Palmeiras]