from teams import times
from functions import simulaJogo
from account import Account
import random

def main():
    
    jogador = Account(0)

    while True:
        print('================================\n' \
              'Bem-vindo a plataforma PETANO!\n' \
              'O que deseja fazer?\n' \
              '1. Depositar\n2. Sacar\n3. Apostar\n4. Saldo\n5. Sair\n' \
              '================================\n')
        
        comando = int(input())

        if comando not in range(1,6):
            print('Comando inválido. Tente novamente.')

        else:
            if comando == 1:
                valor = float(input('Valor a ser depositado: '))
                jogador.saldo += valor
                print(f'Novo saldo: R${jogador.saldo}')

            elif comando == 2:
                valor = float(input('Valor a ser sacado: '))
                if jogador.saldo >= valor:
                    jogador.saldo -= valor
                    print(f'Novo saldo: R${jogador.saldo}')
                else:
                    print('Saldo insuficiente.')
            
            elif comando == 3:
                matchUps = times
                random.shuffle(matchUps)

                bet = float(input('Valor a ser apostado: '))

                if bet <= jogador.saldo:
                    jogador.saldo -= bet

                    print('Qual jogo deseja apostar?\n' \
                        f'1. {matchUps[0].nome.capitalize()} x {matchUps[1].nome.capitalize()}\n' \
                        f'2. {matchUps[2].nome.capitalize()} x {matchUps[3].nome.capitalize()}\n' \
                        f'3. {matchUps[4].nome.capitalize()} x {matchUps[5].nome.capitalize()}\n')
                    
                    escolha = int(input())

                    if escolha == 1:
                        time = input('Resultado: ').lower()
                        if time == simulaJogo(matchUps[0], matchUps[1]):
                            print('Você ganhou!!!')
                            jogador.saldo += 2*bet
                            matchUps[0].gols = 0
                            matchUps[1].gols = 0
                        else:
                            print("Você perdeu!")

                    elif escolha == 2:
                        time = input('Resultado: ').lower()
                        if time == simulaJogo(matchUps[2], matchUps[3]):
                            print('Você ganhou!!!')
                            jogador.saldo += 2*bet
                            matchUps[2].gols = 0
                            matchUps[3].gols = 0
                        else:
                            print("Você perdeu!")

                    else:
                        time = input('Resultado: ').lower()
                        if time == simulaJogo(matchUps[4], matchUps[5]):
                            print('Você ganhou!!!')
                            jogador.saldo += 2*bet
                            matchUps[4].gols = 0
                            matchUps[5].gols = 0
                        else:
                            print("Você perdeu!")
                
                else:
                    print('Você não possui esse valor em seu saldo.')

            elif comando == 4:
                print(f'Saldo: {jogador.saldo}')

            else:
                print('Saindo...')
                break


if __name__ == '__main__':
    main()