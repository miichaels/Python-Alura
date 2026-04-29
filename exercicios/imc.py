peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}')


if imc < 18.5:
    print(f'Peso normal.')
elif imc < 25:
    print(f'Peso normal')
else:
    print(f'Você está acima do peso.')
