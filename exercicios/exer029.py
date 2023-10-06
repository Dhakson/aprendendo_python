#ESCREVA UMA MENSAGEM PARA O MOTORISTA QUE ESTIVER ACIMA DA VELOCIDADE PERMITIDA 

carro = int(input('Qual foi a velocidade do carro? '))
multa = (carro - 80) * 7

if carro <= 80:
    print('Dirija com cuidado!')
elif carro > 80:
    print('Você foi Multado!')
    print(f'O valor da sua multa por excesso de velocidade foi de R$ {multa}')
    