'''CRIE UMA LISTA A ONDE LEIA 5 NÚMEROS DENTRO DE UMA LISTA USANDO O APENDE E MOSTRE 
A POSIÇÃO DO MAIOR NÚMERO E A POSIÇÃO DO MENOR NÚMERO DIGITADO'''

valores = []
menor = maior = 0

for cont in range(0,5):
    valores.append(int(input(f'O número digitado {cont}: ')))
    if cont == 0:
        menor = maior = valores[cont]
    else:
        if valores[cont] > maior:# se o número do contador for maior
            maior = valores[cont]#maior recebe o valor de contador
        elif valores[cont] < menor:
            menor = valores[cont]
print(f'O maior número é {maior}',end=' ')
for c,i in enumerate(valores):
    if i == maior:
        print(f'Está na posição {c}',end=' ')
print()
print(f'O menor número é {menor}',end=' ')
for c, i in enumerate(valores):
    if i == menor:
        print(f'Está na posição {c}',end=' ')