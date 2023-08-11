from random import randint
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('-='*11)

if pc == 0: #pedra
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('você venceu')
    elif jogador == 2:
        print('pc venceu')
    else:
        print('Opção inválida!')
elif pc == 1:#papel
    if jogador == 0:
        print('pc venceu')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('você venceu')
    else:
        print('Opção inválida!')
elif pc == 2:#tesoura
    if jogador == 0:
        print('você venceu')
    elif jogador == 1:
        print('pc venceu')
    elif jogador == 2:
        print('empate')
    else:
        print('Opção inválida!')