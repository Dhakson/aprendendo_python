#CRIE UM PROGRAMA A ONDE PERGUNTA O PESO E ALTURA E CALCAULE A MASSA CORPORAL DE UMA PESSOA (IMC)
peso = float(input('Informe seu Peso em kg: '))
altura = float(input('Informe sa sua altura: '))
imc = peso / (altura ** 2)


print(f' \nO seu IMC é de == {imc:.1f} ==')

if imc <= 16:
    print('\n Magreza Grau 3')
elif imc < 16.9:
    print('\n Magreza Grau 2')
elif imc < 18.4:
    print('\n Magreza grau 1')
elif imc < 24.9:
    print('\n Peso Adequado')
elif imc < 29.9:
    print('\n Pré-Obeso')
elif imc < 34.9:
    print('\n Obesidade Grau 1')
elif imc < 39.9:
    print('\n Obesidade Grau 2')
else:
    print('\n Obesidade Grau 3')
