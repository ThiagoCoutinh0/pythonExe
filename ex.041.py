from datetime import date
n = int(input('Ano de nascimento:'))
idade = date.today().year - n
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')
