salario = float(input('Qual é o salário do funcionário?R$'))
if salario <= 1250:
    aumento= (salario * 15) / 100
else:
    aumento= (salario*10)/100
print('Quem ganhava R${} passa a ganhar R${} agora.'.format(salario,salario+aumento))