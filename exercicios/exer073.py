clubes =('Botafogo','Palmeiras','Bragantino','Grêmio','Flamengo','Fluminense',
         'Atlhetico-PR','Fortaleza','Atletico-MG','Cuiaba','Cruzeiro','Internacional','São Pualo',
         'Corinthians', 'Goiás','Bahia','Santos','Vasco da Gama','America-MG','Coritiba')
print('OS 5 PRIMEIROS COLOCADOS DO BRASILEIRÃO 2023')
for pos,clube in enumerate(clubes[0:5]):
    print(f'{pos+1}ª {clube}')
print(' ')
print('OS ULTIMOS COLOCADOS DO BRASILEIRÃO 2023')
for pos, clube in enumerate(clubes[-4:]):
    print(f'{clube}')
print(' ')
print(f'Os Vasco está em {clubes.index("Vasco da Gama")+1}ª na Tabela do Campeoanato Brsileiro 23')
print(' ')
print(f'{sorted(clubes)}')