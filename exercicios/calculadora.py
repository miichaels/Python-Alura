numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))



tentativas = 3
resultado = None

while tentativas > 0:
    operacao = input("Escolha a operação (| + | - | * | / |):").strip()

    if operacao == "+":
        resultado = numero1 + numero2
        break
    elif operacao == "-":
        resultado = numero1 - numero2
        break
    elif operacao == "*":
        resultado = numero1 * numero2
        break
    elif operacao == "/":
        resultado = numero1 / numero2
        break
    else:
        tentativas -= 1
        print("Operação invalida")

if resultado != None:
    print(f"O resultado pedido é: {resultado}")
else:
    print("Numero de tentativas atingido.")