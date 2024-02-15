lista = []
while True:
    aux = int(input('Digite um número:'))
    if aux not in lista:
        lista.append(aux)
        print('Valor adicionado...')
    else:
        print('Valor duplicado, não vou adicionar...')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break  
lista.sort()
print(lista)



#num = list()
#while True:
#    n = int(input('Digite um valor:'))
#    if n not in num:
#        num.append(n)
#        print('Valor adicionado com sucesso...')
#    else:
#        print('Valor duplicado! Não vou adicionar...')
#    r = str(input('Quer continuar? [S/N]'))
#    if r in 'Nn':
#        break
#num.append()
#print(f'Você digitou os valore {num}')