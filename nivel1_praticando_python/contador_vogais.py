texto = input("Digite uma frase: ")
texto = texto.lower()

contador = 0

for letra in texto:
    if letra in "aeiouáéíóúâêôãõ":
        contador += 1

print(f"A frase contem {contador} vogais")