import datetime
maior = 0
menor = 0
atual = datetime.datetime.now().year
for c in range(7):
    n = int(input('Em que ano a {}° pessoa nasceu:'.format(c+1)))
    if atual - n >= 18:
      maior += 1
    else:
      menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))
