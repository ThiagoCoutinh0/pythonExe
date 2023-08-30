sexo = str(input('Informe seu sexo:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, informe novamente:')).strip().upper()[0]
print('Sexo {} digitado com sucesso!'.format(sexo))
