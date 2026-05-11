def calcular_taxa(entreg):
    if entreg <= 5:
        return "A taxa é 5,00"
    elif entreg <= 10:
        return "A taxa é 8,00"
    else:
        return "A taxa é 10,00"

entreg = int(input("Qual a distancia da entrega? "))
print(calcular_taxa(entreg))


#-------------------------------------
#Adicionando taxa extra
chovendo = (input("Está chovendo? (yes/no): "))
if chovendo == "yes":
    print(True)
else:
    print(False)

entrega = int(input("Qual a distancia da entrega? "))

if entrega <= 5:
    taxa = 5
elif entrega <= 10:
    taxa = 8
else:
    taxa = 10

if chovendo == "yes":
    taxa += 2
    print("Tax adicional de chuva.")
elif chovendo == "no":
    print()

print(f"Taxa total {taxa},00")


