somaidade = 0
maioridadehomem = 0
homemvelho = ''
mulherjovem = 0
for p in range(1, 5):
    print('------{}° pessoa------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M] [F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherjovem += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, homemvelho))
print('Ao todo são {} mulheres mais jovens que 20 anos.'.format(mulherjovem))