# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E INFORME QUAL É O MAIOR E O MENOR
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
menor = num1
#VERIFICANDO O MENOR
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#Verificando o maior
maior= num1
if num2 > num1  and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')