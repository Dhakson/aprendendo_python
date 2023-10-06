extenso = 'Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'
while True:
    numero = int(input('Digite um Número de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente Novamente.',end=' ')

print(f'Você digitou o número: {extenso[numero]}')