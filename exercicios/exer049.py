'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MULTIPLIQUE PELO NÚMERO INFORMADO'''
num = int(input('Digite um número inteiro: '))

print(f'A Tabuada de {num} é: ')
for c in range (0,11):
    print(f'{num} x {c} = {num*c}')