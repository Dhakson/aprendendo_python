# CRIE UM PROGRAMA LEIA O ANO QUALQUER E MOSTRE SE ELE  É BISSEXTO OU NÃO.
from datetime import date
ano = int(input('Qual ano você quer analisar? coloque 0 para o Ano Atual '))
atual= date.today().year
if ano ==0:
    ano = atual 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Esse ano é BISSEXTO {ano}')
else:
    print(f'Esse ano não é BISSEXTO {ano}')