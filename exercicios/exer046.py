#CRIE UM PROGRAMA QUE FAÇA UMA CONTAGEM REGRESSIVA DE 0 A 10 COM INTERVALO ENTRE ELAS DE 1 SEG.

from time import sleep

print('\n  CONTAGEM REGRESSIVA')

sleep(1)
for c in range (0,10):
    sleep(1)
    print(f'\n  {c+1}')