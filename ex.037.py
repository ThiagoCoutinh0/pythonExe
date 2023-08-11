inteiro = int(input(('digite um número inteiro:')))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua escolha:'))

if escolha == 1:
    binario = bin(inteiro)[2:]
    print('{} convertido para BINÁRIO é igual à {}'.format(inteiro,binario))
elif escolha == 2:
    octal = oct(inteiro)[2:]
    print('{} convertido para OCTAL é igual à {}'.format(inteiro,octal))
elif escolha == 3:
    hexadecimal = hex(inteiro)[2:]
    print('{} convertido para HEXADECIMAL é igual à {}'.format(inteiro,hexadecimal))
else:
    print("Opção inválida!")