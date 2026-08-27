#Digite os valores das vendas: 100 250 300

#Saída esperada: O total de vendas foi: 650



valores = input("Digite os valores das vendas: ")

lista_valores = valores.split()

soma = 0

for valor in lista_valores:
    soma = soma + int(valor)

print(f"O total de vendas foi: {soma}")