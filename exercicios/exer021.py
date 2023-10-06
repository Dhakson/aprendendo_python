nome = input('Digite seu nome: ')
print(f'O seu nome em Maisculo fica: {nome.upper()} ') # MAISCULO
print(f'O seu nome em Minusculo fica: {nome.lower()}') # MINUSCULO
print(f'O seu nome com as primeiras letras Maiscula fica: {nome.title()}') # TITULOS
print(f'O seu primeiro nome tem {nome.find(" ")}') # ENCONTRAR
print(f'O seu nome tem  ao total {len(nome) - nome.count(" ")} letras') # COMPRIMENTO e CONTAGEM 