print('Gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA:'))
#decimo = termo + (10-1) * razao
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')