from random import randint
pc = randint(0,5)
eu = int(input('Tente adivinhar o número de 0 a 5:'))
if eu == pc:
    print('Acertou')
else:
    print('Errou')
