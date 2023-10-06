'''CRIE UM PROGRAMA QUE LEIA 5 NÚMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.
DEPOIS DISSO MOSTRE AS LISTAGEM DE NÚMEROS GERADOS E TBM INDIQUE O MAIOR E O MENOR VALOR QUE ESTÃO NA TUPLA'''

from random import randint

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os números Sorteados foram:',end=' ')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')