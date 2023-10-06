'''ESCREVA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE 'M' OU 'F'.
CASO ESTEJA ERRADO,PEÇA A DIGITAÇÃO NOVAMENTE PARA TER UMA RESPOSTA VÁLIDA '''

res = 'MmFf'
n = str(input('Qual é o seu sexo [M/F] ')).strip().upper()[0]
while n not in 'MmFf': #ENQUANTO n NÃO ESTIVER ENTRE 'MmFf" REFAÇA A PERGUNTA NOVAMENTE 
    n = str(input('Sexo Inexistente. Por favor, Informe o seu Sexo [M/N] ')).strip().upper()[0]
print(f'Você é do sexo {n}')