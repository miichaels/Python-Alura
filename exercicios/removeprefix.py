nostarch_url = "https://nostarch.com"


print(nostarch_url)
print()

#removendo prefixo na propria variavel
nostarch_url = nostarch_url.removeprefix("https://")
#removendo prefixo
simple_url = nostarch_url.removeprefix("https://")
print(simple_url)
print()


#------------

arquivo = "python_notes.txt"

nome_sem_extensao = arquivo.removesuffix(".txt")

print(nome_sem_extensao)