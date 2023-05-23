a = float(input('Primero valor:'))
b = float(input('Segundo valor:'))
c = float(input('Terceiro valor:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>a:
    maior = c
print('O menor valor é:{}'.format(menor))
print('O maior valor é:{}'.format(maior))
