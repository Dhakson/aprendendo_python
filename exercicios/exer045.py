#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPO COM VOCÊ.
from time import sleep
from random import randint
itens = ('PEDRA','PAPEL', 'TESOURA')
jogador = int(input('''Escolha uma jogada:
    [1] - PEDRA
    [2] - PAPEL
    [3] - TESOURA
    Qual é a sua Jogada: '''))
print('PEDRA...')
sleep(2)
print('PAPEL...')
sleep(2)
print('TESOURA...')
sleep(2)
computador = randint(0,2)
if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INEXISTENTE')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INEXISTENTE')
elif computador == 2: #TESOURA
    if jogador == 0:
        print("JOGADOR GANHOU")
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INEXISTENTE')
print(f'O jogador {(itens)[jogador]} jogou e computador {(itens)[computador]}')

