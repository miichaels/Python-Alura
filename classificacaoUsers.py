from pprint import pprint

usuarios = {
    "João": 25,
    "Maria": 17,
    "Ana": 19,
    "Carlos": 16,
    "Beatriz": 22,
    "Pedro": 15,
    "Luiza": 18
}

#Classificar
for nome, idade in usuarios.items():
    if idade >= 18:
        print(f"{nome} é adulto")
    else:
        print(f"{nome} é menor")

print()

# classificação usuários

classificacao = {}
for nome, idade in usuarios.items():
    if idade >= 18:
        classificacao[nome] = "adulto"
    else:
        classificacao[nome] = "menor"

pprint(classificacao)
print(classificacao)
print()



# list comprehension
classificacao_usuarios = {
    nome: "adulto" if idade >= 18 else "menor"
    for nome, idade in usuarios.items()
}

print("Classificação dos usuários:")
print(classificacao_usuarios)

