'''CRIE UM PROGRAMA QUE SIMULE UM FUNCIONAMENTO DE UM CAIXA ELETRONICO.
NO INICIO PERGUNTE QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS
DE CADA VALOR SERÃO ENTREGUE'''

saque = int(input("VALOR A SER SACADO R$: "))
ced = 100 #INICIA COM CÉDULA DE 100
totalced = 0 #INCIA A CONTAGEM TOTAL DE CEDULAS
total = saque  #TOTAL RECEBE O VALOR DO SAQUE

while True:
    if total >= ced: #TOTAL FOR MAIOR QUE CÉUDULA
        total -= ced #TENTA TIRAR O MÁXIMO QUE DER DO VALOR TOTAL
        totalced +=1
    else:
        if totalced > 0:
            print(f'FORAM SACADAS {totalced} de R$ {ced:.2f}')
        if ced == 100: #SE NÃO CONSEGUIR TIRAR A MAIOR CEDULA VAI RETIRANDO AS MENORES
            ced =50 
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        totalced = 0 
        if total == 0: #SENÃO TIVER NENHUM VALOR A SER TIRADO ELE PARA2
            break
    