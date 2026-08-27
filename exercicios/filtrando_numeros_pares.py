
filtro = input("Digite os números separados por espaço: ")

filtrando_pares = filtro.split()

pares = []

for valor in filtrando_pares:
    numero = int(valor)

    if numero % 2 == 0: pares.append(str(numero))

print(f"Números pares: {' '.join(pares)}")