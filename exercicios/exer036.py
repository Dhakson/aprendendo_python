#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRESTIMO BANCARIO PARA COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR
#DO IMOVEL,SALARIO E QUANTAS PARCELAS ELE QUER DIVIDIR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELE NÃO PODE EXCEDER 30%
casa = float(input('Valor da Casa - R$: '))
salario = float(input('Informe o Salário - R$: '))
anos = int(input('Em quantos anos quer Pagar? - '))
parcelas = casa / (anos * 12 )
minimo = (salario * 30) / 100

print(f'O valor da casa - R$: {casa:.2f} ')
print(f'O seu salário - R$: {salario:.2f}')
print(f'Qunatidade de Parcelas: {anos} ')
print(f'Valor das Parcelas - R$: {parcelas:.2f}')

if parcelas < minimo:
    print('EMPRESTIMO CONCEDIDO! ')
else:
    print('EMPRESTIMO NEGADO! ')
    