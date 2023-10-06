palavras = ('Python',
            'PyAutogui',
            'Import',
            'Pycharm')

for p in palavras:
    print(f'\nPalvra {p} temos as vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end='')
