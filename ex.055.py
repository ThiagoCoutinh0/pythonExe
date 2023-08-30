maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoa:'.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor= peso
print('A pessoa mais pesada pesa {}kg'.format(maior))
print('A pessoa menos pesada pesa {}kg'.format(menor))