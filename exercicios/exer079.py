'''CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NÚMERICOS 
E CADASTRE-OS EM UMA LISTA, CASO O NÚMERO JÁ EXISTA LÁ DENTRO NÃO SERÁ ADICIONADO'''

lista = []
cont = 0
while True:
    numero = int(input('Digite um número:'))
    if numero not in lista:
        lista.append(numero)
        cont += 1
        lista.sort()
        print('Número Adicionado.')
    else:
        print('Não irei adicionar. Número Repetido')
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer Continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break


print(f'Os números digitados {lista}')
print(f'Foram digitados {cont} números')