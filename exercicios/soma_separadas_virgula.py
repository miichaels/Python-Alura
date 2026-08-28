

produtos = input("Digite os produtos separados por vírgula: ")

lista_produtos = []

for produto in produtos.split(","):
    lista_produtos.append(produto.strip())

precos = input("Digite os preços separados por vírgula: ")
lista_precos = []
for preco in precos.split(","):
    lista_precos.append(preco.strip())


for produtos, precos in zip(lista_produtos, lista_precos):
    print(f"{produtos}: {precos}")