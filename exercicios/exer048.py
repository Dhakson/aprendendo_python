#CRIE UM PROGRAMA QUE LEIA OS NÚMEROS  ÍMPARES DE 1 A 500, MOSTRE A QUANTIDADE E SOME OS NÚMEROS ÍMPARES.
soma = 0
qntd = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += 1
        qntd += c 
print(f'Foram encontrando {soma} de números ímpares,\n e eles somados dão um valor de {qntd}')