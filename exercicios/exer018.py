from math import sin, cos, tan, radians # Randians = para converter Graus em Radianos 

angulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O angulo de {angulo} tem o Seno de : {seno:.2f}')
print(f'O angulo de {angulo} tem o Cosseno de: {cosseno:.2f}')
print(f'O angulo de {angulo} tem a Tangente de: {tangente:.2f}')