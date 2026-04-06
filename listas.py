numeros = [1,2,3,4,5,6,7,8,9,10]

nomes = ["Natalia", "Natanael", "Michael", "Augusto"]

ano = [1997, 2026]

print(f"Imprimindo atividade: \n numeros {numeros} \n nomes: {nomes} \n ano: {ano}")


for numero in numeros:
    print(numero)
print()

soma = 0


for numero in range(1,11):
    if numero % 2 == 0:
        soma = soma + numero

print(f"soma \n")

# Descrescente
for numero in range(10, 0, -1):
    print(numero)