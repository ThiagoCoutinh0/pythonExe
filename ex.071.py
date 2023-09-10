valor = int(input('Que valor você quer sacar R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''print('{:=^40}'.format('BANCO ZAGU'))
saque = 0
while True:
    saque = int(input('Qual valor você quer sacar? R$ '))
    cinquenta = saque // 50
    resto = saque % 50
    vinte = resto // 20
    resto = saque % 20
    dez = resto // 10
    resto = saque % 10
    um = resto // 1
    break

print(f'Total de {cinquenta} cédulas de 50')
print(f'Total de {vinte} cédulas de 20')
print(f'Total de {dez} cédulas de 10')
print(f'Total de {um} cédulas de 1')'''
'''saque = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break
print(f'Você receberá {n50} notas de 50, {n20} de 20, {n10} de 10 e {n1} de 1.')'''