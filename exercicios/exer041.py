'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE A SUA CATEGORIA , DE ACORDO COM A IDADE:
ATÉ 9 ANOS : MIRIM, ATÉ 14 ANOS : INFANTIL, ATÉ 18 ANOS : JUVENIL, ATÉ 20 ANOS : SÊNIOR, ACIMA DE 20 : MASTER '''
from datetime import date
nasc = int(input('Informe a sua data de Nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print(f'sua idade é {idade} anos CATEGORIA - MIRIM')
elif  idade <= 14:
    print(f'sua idade é {idade} anos CATEGORIA - INFANTIL')
elif idade <= 18:
    print(f'Sua idade é {idade} anos CATEGORIA - JUVENIL')
elif idade <= 20:
    print(f'Sua idade é {idade} anos CATEGORIA - SÊNIOR')
elif idade > 20:
    print(f'Sua idade é {idade} anos CATEGORIA - MASTER')

