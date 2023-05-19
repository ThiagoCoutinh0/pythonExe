'''import math
oposto = float(input('Comprimento do cateto oposto:'))
adjacente = float(input('Comprimento do cateto adjacente:'))
hipotenusa = oposto*oposto + adjacente*adjacente
print('A hipotenusa vai medir:{:.2f}'.format(math.sqrt(hipotenusa)))'''
# forma mais abreviada usando math
from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co,ca)
print('A hipotenusa vai medir:{:.2f}'.format(hi))
# forma tradicional sem usar o math
'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir:{:.2f}'.format(hi))'''



