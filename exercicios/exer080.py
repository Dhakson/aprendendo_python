'''CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES
NUMERICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA
DE INSERÇÃO SEM USAR O SORT()
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA'''
lista = []
for c in range (0,5):#irá fazer um range de 5 perguntas
    numeros = int(input(f'Digite um número posição {c}: '))
    # se C for igual a 0 ou numeros maior que a lista -1. Mostrará sempre o ultimo item da lista.
    if c == 0 or numeros > lista[-1]: #se o número for mais que o tamanho da lista ele será o ultimo.
    #será adicionado um número para o final
        lista.append(numeros)
        print('Adicionado ao final da Lista...')
    else:
        pos = 0 #posição inicia com 0
        while pos < len(lista): #enquanto a pos for menor que o tamanho da lista
            if numeros <= lista[pos]: #se o numero for menor ele será adicionado as primeiras posições
                lista.insert(pos, numeros)
                print(f'Foi adicionado na posição {pos}')
                break
            pos += 1 #a cada número adicionado será atribuido a uma posição


print(f'Foram digitados os números {lista}')