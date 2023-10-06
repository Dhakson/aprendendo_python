'''DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. 
E DEPOIS MOSTRE OS 10 PRIMEIROS TERMOS DESSA PA.'''

primeira = int(input('Digite o PRIMEIRO TERMO: '))
razao = int(input('Digite a RAZÃO:'))
exibir = int(input('Quantas vezes que exibir? '))
ultima = primeira + (exibir - 1) * razao
ultima += 1
for c in range(primeira,ultima,razao):
    print(f'{c}',end=' ')