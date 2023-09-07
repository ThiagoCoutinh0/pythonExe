mulheresmenosvinte = 0
homens = 0
maioridade = 0
while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade < 20:
            mulheresmenosvinte += 1
    cont = ' '
    while cont not in 'SN':  # validação de dado
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Total de homens: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheresmenosvinte}')