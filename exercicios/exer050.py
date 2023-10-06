'''CRIE UM PROGRAMA QUE LEIA SEI NÚMEROS E MOSTRE APENAS A SOMA DAQUELES QUE FOREM PARES. 
SE O VALOR DIGITADO FOR ÍMPAR DESCONSIDERE-O.'''
impar = 0 
soma = 0
cont = contimpar = 0
for c in range (6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
    else:
        if numero % 2 == 1:
            impar += numero
            contimpar += 1

print(f'Foram digitados {cont} números pares. A soma entre eles {soma}')
print(f'Foram digitados {contimpar} números ímpares. A soma entre eles {impar}')