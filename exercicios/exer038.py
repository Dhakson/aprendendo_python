'''ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E OS COMPARE-OS MOSTRANDO A MENSAGEM NA TELA:
   O PRIMEIRO NUMERO É MAIOR - O SEGUNDO NÚMERO É MAIOR - NÃO EXISTE VALOR MAIOR, OS DOIS NÚMEROS SÃO IGUAIS '''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número:  '))
#DEFINE O MAIOR NÚMERO
if num1 > num2 or num2 < num1:
    maior = num1
    print('O Primeiro número é Maior! ')
elif num2 > num1 or num1 < num2:
    maior = num2
    print('O Segundo número é Maior! ')
elif num1 == num2:
    print('Não á numero maiores, os numeros são iguais. ')
#DEFINE O MENOR NÚMERO
if num1 < num2 or num2 > num1:
    menor = num1
    print('O Primeiro Número é Menor')
elif num2 < num1 or num1 > num2:
    menor = num2
    print('O Segundo número é Menor')
elif num1 == num2:
    print('Não á numéro menor, os números são iguais.')
