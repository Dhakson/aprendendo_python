'''CRIE UMA OPÇÃO DE MENUS '''

valor = int(input('PRIMEIRO VALOR: '))
valor2 = int(input('SEGUNDO VALOR: '))
opcao = 0
while opcao != 7:
    print('''ESCOLHA OPÇÃOES ABAIXO \n[1] - SOMAR \n[2] - SUBTRAIR \n[3] - MULTIPLICAR \n[4] - DIVIDIR \n[5] - MAIOR \n[6] - NUMEROS NOVOS \n[7] - SAIR''')
    opcao = int(input('opção: '))
    if opcao == 1:
        soma = valor + valor2
        print(f'A Soma dos valores {valor} + {valor2} = {soma}')
    elif opcao == 2:
        subtrair = valor - valor2
        print(f'Os valores subtraidos {valor} - {valor2} = {subtrair}')
    elif opcao == 3:
        mult = valor * valor2
        print(f'Os valores Multiplicados {valor} x {valor2} = {mult}')
    elif opcao == 4:
        dividir = valor / valor2
        print(f'Os valores divididos {valor} / {valor2} = {dividir}')
    elif opcao == 5:
        if valor > valor2:
            maior = valor
            print(f'O Maior valor é {valor}')
        elif valor2 > valor:
            maior = valor2
            print(f'O Maior valor é {valor2}')
    elif opcao == 6:
        print('Informe os Números Novos')
        valor = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo Valor: '))
    elif opcao == 7:
        print('OBRIGADO POR ACESAR MEU APP! ')
    else:
        print('OPÇÃO INVALIDA')

print('VOLTE SEMPRE!')