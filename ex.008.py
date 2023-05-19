d = float(input('Digite a distância em metros:'))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('A média de {} corresponde a \n {}km \n {}hm \n {}dam \n {:.0f}dc \n {:.0f}cm \n {:.0f}mm'.format(d,km,hm,dam,dm,cm,mm))