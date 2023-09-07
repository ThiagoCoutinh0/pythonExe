mult = 0
while True:
    print('-'*33)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    mult += 1
    for mult in range(1,11):
        print(f'''{n} x {mult} = {n * mult}''')
print('Programa tabuada encerrado!')

#Ou

'''while True:
    n = int(input('Quer ver aa tabuada de qual valor? '))
    print('-' * 33)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 33)
print('Programa encerrado.')'''