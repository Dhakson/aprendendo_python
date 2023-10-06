'''CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS
E COLOCAR EM UMA LISTA
DEPOIS MOSTRE:
A- QUANTOS NÚMEROS FORAM DIGITADOS
B- A LISTA DE VALORES EM ORDEM DECRESCENTE
C- SE O VALOR 5 FOI DIGITADO E ESTÁ OU NA LISTA'''

lista = [ ]
while True:
    lista.append(int(input('Digite um número: ')))
    lista.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer Continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break

if 5 not in lista:
    print("O número 5 não está na lista")
else:
    print("O número 5 está na lista ")