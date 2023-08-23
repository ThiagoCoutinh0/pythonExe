print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

termo = int(input('Primeiro termo:'))
razao = int(input('razão'))
decimo = termo + (10-1) * razao
for c in range(termo,decimo + razao,razao):
    print('{}'.format(c), end=' \u2192 ')
print('ACABOU')

#OU

"""termo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
pa = 0
for c in range(1,10):
    termo+=razao
    print(termo, end=' \u2192 ')
print('ACABOU')"""
