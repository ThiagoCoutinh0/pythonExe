valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
exceder = salario * 0.30
prestacao = valor / (anos*12)
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(valor,anos,prestacao))

if prestacao > exceder:
    print('Impréstimo NEGADO!')
else :
    print('Impréstimo APROVADO!')