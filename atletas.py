atletas = [
    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 59],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 61],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]


# for nome, altura, peso in atletas:
#     print(f"Nome: {nome}")
#     print(f"Altura: {altura} m")
#     print(f"Peso: {peso} kg")
#     print("-------------------")



# funciona porém é menos usado:
"""  
    for atleta in atletas:
    print(f"Nome: {atleta[0]}")
    print(f"Altura: {atleta[1]} m")
    print(f"Peso: {atleta[2]} kg")
"""


# Lista para armazenar as tuplas
atletas_tuplas = []

# Loop para converter cada sublista em uma tupla
for atleta in atletas:
    nome = atleta[0]
    altura = atleta[1]
    peso = atleta[2]

    atleta_tupla = (nome, altura, peso)  # Criação da tupla
    atletas_tuplas.append(atleta_tupla)  # Adição da tupla na nova lista

# Impressão da lista de tuplas
print(atletas_tuplas)
print(atleta_tupla)


#--------------------------------------------------------------------------------

# Cálculo da altura média utilizando list comprehension
alturas = [atleta[1]
for atleta in atletas]  # Extração das alturas
altura_media = sum(alturas) / len(alturas)  # Cálculo da média

# Impressão do resultado
print(f"A altura média dos atletas é: {altura_media:.2f} metros")

alturas = [atleta[1] for atleta in atletas]



# Cálculo do IMC e identificação de atletas com IMC > 25
atletas_sobrepeso = [atleta[0] for atleta in atletas if (atleta[2] / (atleta[1] ** 2)) > 23]

print("Atletas com IMC maior que 25:")
print(atletas_sobrepeso)

