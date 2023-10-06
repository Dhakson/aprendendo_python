# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E INFORME SE É PAR OU ÍMPAR!
print('=-' * 30)
print('Jogue um número e falarei se é PAR ou ÍMPAR')
print('=-' * 30)
numero = int(input('Digite um número inteiro: '))
resultado = numero % 2 # NUMERO DIVIDO PELO RESTO 

if resultado == 0:
    print(f'O Número {numero} que você jogou é PAR')
else:
    print(f'O Número {numero} que você jogou é ÍMPAR')