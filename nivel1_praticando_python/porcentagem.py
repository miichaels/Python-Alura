conta = float(input("Digite o valor da conta: "))

gorjeta = float(input("Digite o valor da gorgeta: "))


def calcular_gorgeta(gorgeta):
    return conta * gorgeta / 100

valor_gorjeta = calcular_gorgeta(gorjeta)
precoFinal = conta + valor_gorjeta

print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {precoFinal:.2f}")