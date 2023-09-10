print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)
tot = 0
maismil = 0
produto_mais_barato = None  # Variável para armazenar o produto mais barato
preco_mais_barato = float('inf')  # Inicialize o preço mais barato com um valor infinito
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    tot += preco

    # Verifica se o preço é menor do que o preço mais barato atual
    if preco < preco_mais_barato:
        produto_mais_barato = produto
        preco_mais_barato = preco

    if preco >= 1000:
        maismil += 1

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-'*20 , end=' ')
print('FIM DO PROGRAMA', end=' ')
print('-'*20 ,)
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {maismil} produto(s) custando mais de 1000')
print(f'O produto mais barato foi {produto_mais_barato} custando R${preco_mais_barato}')
