num = 0
cont = 0
parada = ''
while parada != 'n':
    num = int(input('Digite um número: '))
    parada = str(input('Quer continuar;'))
    num += num
    cont += 1
    media = num / cont
print(num, cont, media)

