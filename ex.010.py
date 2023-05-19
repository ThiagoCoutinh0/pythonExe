#cash = float(input('Quanto dinheiro você tem na carteira? R$'))
#euro = 0.18
#real = euro * cash
#print('Com R${} você pode comprar {:.2f} Euros'.format(cash,real ))

real = float(input('Quanto dinheiro você tem na carteira? R$'))
euro = real / 5.57
print('Com R${} você pode comprar {:.2f} Euros'.format(real,euro))