from random import randint
pc = randint(1,10)
print('Sou seu computador e acabei de pensar em número entre 1 e 10. ')
print('Adivinhe qual foi! ')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez:')
        elif jogador > pc:
            print('menos... Tente mais uma vez:')
print('Acertou com {} tentativas. Parabéns'.format(tentativas))



''' meu jeito abreviado
from random import randint
pc = randint(1,10)
eu = int(input('Tente adivinhar um número de 1 a 10:'))
tentativas = 0
while eu != pc:
    if eu < pc:
        eu = int(input('mais:'))
        tentativas += 1
    if eu > pc:
        eu = int(input('menos:'))
        tentativas += 1
print('acertou')
print(tentativas)'''