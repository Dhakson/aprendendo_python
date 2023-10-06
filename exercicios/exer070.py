'''CRIE UM PROGRAMA ONDE LEIA O NOME E O VALOR DE VÁRIOS PRODUTOS. 
O PROGRAMA DEVERÁ PERGUNTAR SE O CLIENTE QUER COTNINUAR SIM OU NÃO.
NO FINAL MOSTRAR: 
1- O VALOR TOTAL DAS COMPRAS, 2 - QUAL O PRODOUTO QUE CUSTA MAIS 1.000 REAIS 3 - E QUAL É O PRODUTO MAIS BARATO'''
total = 0
mais_de_mil = 0
cont = 0
menor = 0
while True:
    produto = input('Produto: ')
    preco = int(input('Preço R$: '))
    total += preco
    cont += 1
    if preco >= 1000:
        mais_de_mil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor :
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer Continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break
print(f'TOTAL DAS COMPRAS {total:.2f}')
print(f'EXISTEM {mais_de_mil} ACIMA DE R$ 1.000,00')
print(f'O PRODUTO MAIS BARATO CUSTA R${menor:.2f}')