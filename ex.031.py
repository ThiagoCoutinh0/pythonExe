d = float(input('Quantos km é a sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
preço = d * 0.5 if d <= 200 else d * 0.45
'''if d <= 200:
    preço = d * 0.5
else:
    preço = d * 0.45'''
print('O preço da sua passagem vai ser de R${:.2f}'.format(preço))