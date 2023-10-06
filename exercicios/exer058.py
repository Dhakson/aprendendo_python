'''JOGO DA ADVINHAÇÃO COM O WHILE '''

from random import randint
jogador = int(input('Advinhe um Número: '))
computador = randint (0,10)
qntd = 0 
while jogador != computador: #ENQUANTO JOGADOR FOR DIFERENTE DO COMPUTADOR REPITA A PERGUNTA ATÉ ACERTAR
    if computador != jogador:
        jogador = int(input('Tente novamnte: '))
        qntd += 1 #RECEBE MAIS - PARA SABER A QUANTIDADE DE ADVINHAÇÃO FORAM FEITAS
    if jogador == computador:
        print('Você Ganhou!!!')

print(f'Você jogou o número {jogador} e computador jogou o número {computador}')
print(f'Você jogou {qntd} duas vezes para ganhar do Computador')
