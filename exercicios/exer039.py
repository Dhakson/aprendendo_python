'''ESCREVA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM A SUA IDADE:
SE ELE IRÁ SE ALISTAR - SE JÁ PASSOU DA HORA DE SE ALISTAR - JÁ PASSOU O TEMPO DE ALISTAMENTO.
O PROGRAMA TAMBÉM DEVERÁ MOSTRAR QUANTO TEMPO FALTA E QUANTO TEMPO JÁ PASSOU PARA O ALISTAMENTO'''
from datetime import date
nasc = int(input('Informe o Ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'Você tem {idade} anos')

if idade == 18:
    print('Você precisa se Alistar!')
elif idade < 18:
    falta = 18 - idade
    print(f'Você não precisa se Alistar. Ainda faltam {falta} anos para o seu Alistamento.')
elif idade > 18:
    falta = idade - 18
    print(f'Você passou {falta} anos do seu Alistamento. Procure uma Junta Militar e Regularize a sua situação.')