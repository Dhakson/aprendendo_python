#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM COBRANDO R$ 0,50,
#POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45 PARA VIAGEM MAIS LONGA
print('VIAGEM MAIS TOUR')
distancia = float(input('Quantos KM será feita a viagem: '))
valor1 = distancia * 0.50
valor2 = distancia * 0.45
if valor1 <= 200:
    print(f'O valor cobrado por {distancia}Km será de R$ {valor1}')
elif valor2 > 200:
    print(f'A sua viagem acima de 200Km, ficará no valor de R$ {valor2:.2f} ')