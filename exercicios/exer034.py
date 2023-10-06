#ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO ATUAL DO FUNCIONARIO E CALCULE O SEU AUMENTO.
#PARA SALARIOS ACIMA DE 1.500 REAIS AUMENTE 10%
#PARA SALARIO ABAIXO DE 1.500 REAIS AUMENTE 15%
from time import sleep
salario = float(input('Informe o salario funcionario - R$:  '))

if salario <= 1500:
    novo_salario = salario + (salario * 15 / 100)
    aumento_percentual = 15
    aumento_salario = (aumento_percentual * salario) /100
else:
    novo_salario = salario + (salario * 10 / 100)
    aumento_percentual = 10
    aumento_salario = (aumento_percentual * salario) / 100
sleep (1)
print('=-' * 30)
print(f'Quem recebia o salario de {salario:.2f} passa a receber {novo_salario:.2f}') 
print('=-' * 30)
sleep (1)
print(f'O aumento percentual sobre seu salario foi de {aumento_percentual}%')
sleep (1)
print('=-' * 30)
print(f'O seu salario teve um acrescimo de {aumento_salario:.2f}')
print('=-' * 30)