palavras = ('linguagem','python','estudos','viagens','liberdade')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

#solução de inscrito
'''palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco', 'cachorro', 'tabuada', 'paraguai', 'esquecido')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in range(0, len(palavras)):
    print(f'Na palavra "{palavras[c].upper()}", encontramos as vogais: ', end='')
    for v in range(0, len(vogais)):
        if vogais[v] in palavras[c]:
            print(end=f'{vogais[v].upper()} ')
    print('')'''
