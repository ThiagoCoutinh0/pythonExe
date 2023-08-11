gasto = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção?'))

if opcao == 1:
    print('Sua compra de R${} vai custar R${} no final'.format(gasto,gasto-gasto*0.10))
elif opcao == 2:
    print('Sua compra de R${} vai custar R${} no final'.format(gasto, gasto - gasto * 0.05))
elif opcao == 3:
    print('Sua compra de R${} vai custar R${} no final'.format(gasto, gasto))
elif opcao == 4:
    quantas = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}x COM JUROS'.format(quantas))
    print('Sua compra de R${} vai custar R${} no final'.format(gasto, gasto + (gasto*0.20)))
else:
    print('Opção inválida!')