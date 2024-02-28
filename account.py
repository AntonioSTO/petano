import functions

class Account:
    def __init__(self,saldo):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor
        print(f"Você sacou R${valor}!")

    def bet(self,valor, aposta, time1,time2):
        self.saldo -= valor

        if aposta == functions.simulaJogo(time1,time2):
            print(f'Boa Pet...digo, BET!!!\nVocê ganhou {2*valor}!')
            self.saldo += 2*valor

        else:
            print('Não foi dessa vez...')
    
