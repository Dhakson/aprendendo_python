'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA.
NO FINAL,MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR '''

lista = ('pão',3.75,
         'Queijo',8.90,
         'Presunto',10.50)

print('-'*90)
print('{:^90}'.format('\033[1;32mLISTA DE COMPRAS\033[m'))
print("-"*90)
#print('{:^90}'.format('\033[1;32mLISTAGEM DE PREÇOS\033[m'))
for pos in range(0,len(lista),2):
    print(f'{lista[pos]:.<30}',end=' ')
    print(f'R${lista[pos+1]:>7.2f}')
