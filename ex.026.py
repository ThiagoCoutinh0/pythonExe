frase = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('A')+1))