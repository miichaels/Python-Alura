# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for lista in lista_de_compras:
    print("- " + lista)



# Definindo uma tupla de coordenadas geográficas  (Fixa)
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("\nCoordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])