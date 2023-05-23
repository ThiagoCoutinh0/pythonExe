a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a<b+c and b<a+c and c<a+b:
    print('OS segmentos acima formam um triângulo')
else:
    print('Os segmentos não formam um triângulo')