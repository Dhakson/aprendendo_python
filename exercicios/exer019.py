from random import choice # Sorteia aleatoriamente 
from time import sleep

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
lista = [n1, n2 , n3, n4]
escolhido = choice(lista)

print("==="*30)
sleep(1)
print('Saindo o resultado...')
sleep(1)
print("==="*30)
print(f'O aluno escolhido foi? {escolhido}.')