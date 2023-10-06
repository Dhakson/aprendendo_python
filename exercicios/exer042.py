reta1 = int(input('Primeira Reta: '))
reta2 = int(input('Segunda Reta: '))
reta3 = int(input('Terceira Reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f' As retas {reta1} + {reta2} + {reta3} Formam um Triangulo', end=' ')
    if reta1 ==  reta2  and reta2 == reta3:
        print('EQUILATERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('As retas não formam um triângulo')
