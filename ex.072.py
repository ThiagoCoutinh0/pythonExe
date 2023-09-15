extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[num]}')

#outra forma

'''extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
for n in enumerate(extenso):
    n = int(input('Digite um número entre 0 e 10: '))
    if n <= 10:
        print(f'Você digitou o número {extenso[n]}')
        break
    else:
        print('Tente novamente. ', end='')'''
