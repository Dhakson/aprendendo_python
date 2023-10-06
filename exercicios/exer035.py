#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E QUE INFORME SE FAZ UM TRAINGULO OU NÃO

reta = int(input('Primeira Reta: '))
reta_2 = int(input('Segunda Reta: '))
reta_3 = int(input('Terceira Reta: '))


if reta < reta_2 + reta_3 and reta_2 < reta + reta_3 and reta_3 < reta +reta_2:
    print(f'A retas {reta} , {reta_2} e {reta_3} formam um triangulo ')
    
else: 
    print(f'As retas {reta} ,{reta_2} e {reta_3} não formam um triangulo')