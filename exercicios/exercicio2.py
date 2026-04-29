A = int(input('Digite o tempo em dias para o item A: '))
B = int(input('Digite o tempo em dias para o item B: '))
C = int(input('Digite o tempo em dias para o item C: '))

soma = A + B + C


if (A >= 0 and B >= 0 and C >= 0):
    tempo_total = A + B + C
    print(f'A soma total do tempo é de {tempo_total} dias')
else:
    print('Os dias não podem ser negativos')