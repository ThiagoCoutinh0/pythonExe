lista = []

for c in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {c}:'))
    lista.append(valor)

print(f'Você digitou os valores {lista}')

menor = min(lista)
maior = max(lista)

indices_menor = [i for i, x in enumerate(lista) if x == menor]
indices_maior = [i for i, x in enumerate(lista) if x == maior]

print(f'O menor valor digitado foi {menor} nas posições {indices_menor}')
print(f'O maior valor digitado foi {maior} nas posições {indices_maior}')
