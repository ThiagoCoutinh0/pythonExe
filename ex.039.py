from datetime import datetime
anoatual = datetime.now().year
nasceu = int(input('Qual ano você nasceu?'))
idade = anoatual - nasceu
falta = 18-idade
passou = abs(falta)

if idade < 18:
   print('Quem nasceu em {} tem {} anos em {}.'.format(nasceu,idade,anoatual))
   print('Ainda faltam {} anos para o alistamento militar.'.format(falta))
   print('Seu alistamento será em {}.'.format(datetime.now().year+falta))
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasceu,idade,anoatual))
    print('Você deveria ter se alistado há {} anos.'.format(passou))
    print('Seu alistamento foi em {}.'.format(datetime.now().year-passou))
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasceu, idade, anoatual))
    print('Você deve se alistar IMEDIATAMENTE!')

#eu poderia ter simplificado colocando o primeiro print fora das condições e uma variavel "ssaldo" dentro das condições para verificar a diferença.
# outra opção mais elaborada:
from datetime import date

sexo = input('Digite o seu sexo: ').strip().upper()

if sexo == 'FEMININO':
    print('Seu alistamento é opcional')
    desejo = input(('Você deseja se alistar? (S ou N) ')).strip().upper()
    if desejo == 'S':
        ano = int(input('Digite o ano que você nasceu: '))
        idade = date.today().year - ano
        if idade < 18:
            print(f"Você nasceu em {ano} e sua idade é {idade} anos")
            saldo = 18 - idade
            ano = saldo + date.today().year
            print(f'\033[33mVocê irá se alistar em {ano}\033[m')
        elif idade == 18:
            print(f"Você nasceu em {ano} e sua idade é {idade}")
            print('\033[31mVocê deve se alistar agora\033[m')
        else:
            print(f"Você nasceu em {ano} e sua idade é {idade}")
            saldo = idade - 18
            ano = date.today().year - saldo
            print(f'\033[32mJá passou {saldo} anos hora de se alistar\033[m')
            print(f'Você deveria ter se alistado em {ano}')
    else:
        print('Muito obrigado pela sua resposta.')

elif sexo == 'MASCULINO':
    ano = int(input('Digite o ano que você nasceu: '))
    idade = date.today().year - ano
    if idade < 18:
        print(f"Você nasceu em {ano} e sua idade é {idade} anos")
        saldo = 18 - idade
        ano = saldo + date.today().year
        print(f'\033[33mVocê irá se alistar em {ano}\033[m')
    elif idade == 18:
        print(f"Você nasceu em {ano} e sua idade é {idade}")
        print('\033[31mVocê deve se alistar agora\033[m')
    else:
        print(f"Você nasceu em {ano} e sua idade é {idade}")
        saldo = idade - 18
        ano = date.today().year - saldo
        print(f'\033[32mJá passou {saldo} anos hora de se alistar\033[m')
        print(f'Você deveria ter se alistado em {ano}')
else:
    print('Opção inválida.')
