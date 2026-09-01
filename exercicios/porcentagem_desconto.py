desconto = float(input("Digite a porcentagem de desconto: "))

valorCompra = float(input("Digite o valor da compra: "))

precoFinal = valorCompra - (valorCompra * desconto / 100)

print(f"Preço final com desconto: {precoFinal}")