# lista = []

# for c in range(0, 5):
#     valor = int(input(f'Digite um valor para a posição {c}:'))
#     lista.append(valor)

# print(f'Você digitou os valores {lista}')

# menor = min(lista)
# maior = max(lista)

# indices_menor = [i for i, x in enumerate(lista) if x == menor]
# indices_maior = [i for i, x in enumerate(lista) if x == maior]

# print(f'O menor valor digitado foi {menor} nas posições {indices_menor}')
# print(f'O maior valor digitado foi {maior} nas posições {indices_maior}')

lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else: 
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O maior número foi {maior} nas posições', end=' ' )
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')