#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# 1 PARA BINÁRIO , 2 OCTAL , 3 HEXADECIMAL 

num = int(input('Digite um número para converter: '))
print ('''[1] - BINARIO \n[2] - OCTAL \n[3] - HEXADECIMAL''')
opcao = int(input('Qual é a sua opção: '))
while opcao != (1,2,3):
    opcao = int(input('Informe um Opção valida: '))
    if opcao == 1:
        print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}')
    elif opcao == 2:
        print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
    elif opcao == 3:
        print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}')
    break
    
