def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ",.!?;:\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
        return texto

def contar_palavras(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)