'''CRIE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO CONSIDERANDO SEU PREÇO NORMAL E A FORMA DE PAGAMENTO.'''
print('     === LOJAS FULEIRAGEM ===   ')
valor_produto = float(input('Informe o valor do Produto - R$: '))
opcao = int(input('''Escolha uma forma de pagamento:
[1] - Á vista
[2] - Débito/Pix
[3] - Em 2x no Cartão de Crédito 
[4] - Em 3x ou mais no Cartão de Crédito
Opção =  '''))
if opcao == 1:
    valor_pago = valor_produto - (valor_produto * 10 / 100)
    print('você teve um desconto de 10%.'f'\nO valor total a ser pago  R$: {valor_pago:.2f}')
elif opcao == 2:
    valor_pago = valor_produto - (valor_produto * 5 / 100)
    print(f'Você obteve 5% de desconto.\nO valor total a ser pago R$: {valor_pago:.2f}')
elif opcao == 3:
    print(f'Não há juros até em 2x no cartão.\nO valor total a ser pago R$: {valor_produto:.2f}')
elif opcao == 4:
    valor_pago = valor_produto + (valor_produto * 20 / 100)
    parcela = int(input("\nEm quantas parcelas será pago? "))
    total = valor_pago / parcela
    print(f'''Acima de 3x o valor da compra fica 20% mais caro.
        \nO valor a ser pago R$: {valor_pago:.2f}
        Ficará com parelas {parcela}x de R$: {total:.2f}''')
else:
    print('Opção Incorreta!\nEscolha uma Opção certa para prosseguir.')