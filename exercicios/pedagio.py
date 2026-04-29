km = int(input('Digite a distância percorrida em km: '))

if km <= 100:
    print('Valor do pedágio: R$ 10,00')
elif km <= 200:
    print('Valor do pedágio: R$ 20,00')
else:
    print('Valor do pedágio: R$ 30,00')