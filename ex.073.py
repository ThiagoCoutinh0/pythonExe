tabela = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino',
          'Athletico - PR', 'Fortaleza', 'Atlético - MG', 'Cuiabá', 'São Paulo',
          'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos',
          'Vasco', 'América - MG', 'Coritiba')
print('=-='*20)
print(f'Lista dos times do brasileirão: {tabela}')
print('=-='*20)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('=-='*20)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('=-='*20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('=-='*20)
print(f'O Internacional está na {tabela.index("Internacional")+1}° posição.')