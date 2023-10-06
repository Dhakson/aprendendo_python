'''CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A SUA MÉDIA, MOSTRANDO UMA MENSAGEM, DE ACORDO COM A MÉDIA
MEDIA ABAIXO 5 - REPROVADO, MÉDIA ENTRE 5 E 6.9 - RECUPERAÇÃO, MÉDIA ACIMA DE 7 APROVADO.'''

nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'As notas {nota1} + {nota2} somadas deram uma média de {media}')
if media >= 7:
    print('APROVADO!')
elif media < 4.9:
    print('REPROVADO!')
elif media < 6.9:
    print('RECUPERAÇÃO!')

