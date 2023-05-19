preco = float(input('Qual é o preço do produto? R$'))
desconto = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção de 5% passou a custar R${:.2f}'.format(preco,desconto))