'''from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')'''

#Jeito do curso em vídeo
from random import randint
numeros = (randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f' O menor valor sorteado foi {min(numeros)}')

#Criado pelo Bing mas usa list comprehension para gerar a tupla de números aleatórios
'''from random import randint
numeros = tuple(randint(1,10) for _ in range(5))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f' O menor valor sorteado foi {min(numeros)}')'''