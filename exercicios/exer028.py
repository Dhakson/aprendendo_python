# ESCREVA UM PROGRAMA E FAÇA COMPUTADOR PENSAR UM NÚMERO INTEIRO ENTRE 0 E 5
# O usuario tentará acertar qual foi o numero do computador 
from random import randint # Randoniza número inteiro
from time import sleep
print('=*'*30)
print('Vou pensar em número. tente adivinhar...')
sleep(1)
print('=*'*30)
jogador1 = int(input('Advinhe o Número: ')) # JOGADOR TENTA ADVINHA O NÚMERO DO COMPUTADOR.
sleep(1)
print('Processando...')
computador = randint (0, 5) # O COMPUTADOR IRÁ "PENSAR" EM QUAL NÚMERO IRA JOGAR
if jogador1 == computador: #SE O JOGADOR JOGAR O MESMO NÚMERO ELE GANHA
    print('Você ganhou!')
if computador != jogador1: #SE O NÚMERO FOR DIFERENTE O JOGADOR IRÁ ADIVINHAR O NÚMERO
    print('Você Perdeu')
            

print(f'Você jogou {jogador1} e o computador jogou {computador}')