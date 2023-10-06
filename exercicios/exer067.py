'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E INFORME A TABUADA DO NÚMERO INFORMADO USANDO WHILE'''
while True:#GERA UM LOOP ETERNO 
    print('=-'*30)
    numero = int(input('Informe um Número: ')) #PERGUNTA O NÚMERO INTEIRO PARA GERAR A TABUADA
    print('=-'*30)
    if numero < 0: #SE O NÚMERO FOR INVALIDO EX: -1. O PROGRAMA IRÁ PEDIR UM NÚMERO VALIDO PARA CONTINUAR
        numero = int(input('Informe um Número Valido: '))
        print('=-'*30)
    elif numero == 999:#SE O NÚMERO FOR 999 O PROGRAMA SERÁ ENCERRADO 
        break
    for c in range (0,10):#IRÁ CONTAR ATÉ 10 E ASSIM GERANDO A TABUADA DO NÚMERO INFORMADO
        print(f'{numero} x {c + 1} = {numero * c}') 
print('PROMGRAMA ENCERRADO!')