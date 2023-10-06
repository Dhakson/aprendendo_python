'''CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR
SE O USUÁRIO QUER CONTINUAR OU NÃO. NO FINAL,MOSTRE:'''
'''QUANTAS PESSOAS TEM MAIS DE 18 ANOS
QUANTOS HOMEMS FORAM CONTRATADOS
QUANTAS MULHRE TEM MENOS DE 20 ANOS'''
Homem = 0
mulher20 = 0 
qntd = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('SEXO [M/F]: ').strip().upper()[0]
    if sexo == 'M':
        Homem += 1
        qntd += 1
    elif sexo == 'F' and idade <= 20:
        mulher20 += 1
        qntd += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('QUER CONTINUAR [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print('VOLTE SEMPRE')
print(f'Foram Cadastrados {Homem} homens ')
print(f'Foram Cadastradas {mulher20} mulheres abaixo dos 20 anos')
print(f'Foram Cadastradas {qntd} no Sistema')