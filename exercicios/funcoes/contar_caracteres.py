def contar_caracteres(palavra):
    return len(palavra)

texto = input('Digite uma letra: ')

print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.")