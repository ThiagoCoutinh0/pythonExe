'''import math
valor = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(valor, math.trunc(valor)))'''
#outra forma de fazer é
from math import trunc
valor = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(valor, trunc(valor)))
#Outra forma de fazer sem usar o import é
'''valor = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(valor,int(num)))'''
