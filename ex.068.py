from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0,11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI': #validação de dado
        tipo = str(input('PAr ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria +=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')






'''from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
escolha = ''
aux = ''
while True:
    pc = randint(1,9)
    eu = int(input('Diga um valor: '))
    escolha = str(input('PAR OU ÍMPAR? [P/I]')).strip().upper()
    soma = pc + eu
    print(f'Você jogou {eu} e computador {pc}. Total de {soma},')
    if soma % 2 == 0:
        aux = 'P'
    else:
        aux = 'I'
    if escolha == aux:
        print('venceu')
        break
    else:
        print('Perdeu')
    print(escolha)
    print(aux)'''
