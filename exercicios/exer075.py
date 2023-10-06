'''DESENVOLVA UM PROGRAMA QUE LEIA 4 VALORES PELO TECLADO E GUARDE EM UMA TUPLA E NO FINAL MOSTRE:
1 - QUANTA VEZES MOSTROU O NÚMERO 9
2 - EM QUE POSIÇÃO FOI DIGITADO O NÚMERO 3 
3 - E QUAIS FORAM OS NÚMEROS PARES'''

numeros = (int(input('Primeiro Número: ')),int(input('Segundo Número: ')),
           int(input('Terceiro Número: ')),int(input('Quarto Número: ')),)

if 9 in numeros:
    print(f'O Número 9 apareceu {numeros.count(9)} vezes.')
else:
    print('O Número 9 não apareceu.')

if 3 in numeros:
    print(f'O Número 3 está na {numeros.index(3)+1}ª Posição')
else:
    print('O Número 3 não foi encontrado.')

for num in numeros:
    if num % 2 == 0:
        print(f'Os Números Pares são {num}')