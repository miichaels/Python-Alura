numero = -1
#loop rodara 3 tentativas para obter um numero positivo número máximo de tentativas (3)
for _ in range(3):
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)



#loop irá rodar até obter um numero positivo
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)