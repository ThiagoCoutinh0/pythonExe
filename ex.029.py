#condição simples
velocidade= float(input('Digite a sua velocidade:'))
if velocidade > 80:
    print('Multado, Você excedeu o limite de velocidade!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar o valor de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança.')


'''velp = 80
vel = int(input('Qual a sua velocidade?'))
multa = (vel - 80) * 7
if vel <= velp:
    print('Velocidade permitida, tenha uma boa viagem!')
else:
    print('Multado! o valor da multa é R${}'.format(multa))'''