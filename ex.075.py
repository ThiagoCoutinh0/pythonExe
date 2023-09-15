#Curso em Video
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

#tentando sozinho
'''valor1 = input('Digite o primeiro número: ')
valor2 = input('Digite o segundo número: ')
valor3 = input('Digite o terceiro número: ')
valor4 = input('Digite o quarto número: ')
tupla = ([valor1,valor2,valor3,valor4])
print(f'Você digitou os valores : {tupla}')
print(f'O valor 9 foi digitado {tupla.count("9")} vezes.')
print(f'O valor 3 apareceu na {tupla.index("3")+1}° posição.')'''
