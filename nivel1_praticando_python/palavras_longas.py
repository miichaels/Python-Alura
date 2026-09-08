texto = input("Digite seu texto: ")
texto = texto.lower()

palavras_longas = []

palavras = texto.split() #separa o texto em palavras

for palavra in palavras:
    if len(palavra) > 10: #conta quantas letras uma palavra tem
        palavras_longas.append(palavra) #adiciona a palavra na lista palavras_longas

if len(palavras_longas) > 0:
    palavras_formatadas = ", ".join(palavras_longas) #Junta as palavras da lista, separando cada uma por vírgula e espaço
    print(f"Palavras longas encontradas: {palavras_formatadas}")
else:
    print(f"Nenhuma palavra longa foi encontrada no texto.")


