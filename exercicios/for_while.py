#Imprima a lista clientes
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

#---------------------

#corrija o loop infinito
contador = 0

while contador < 5:
    print("Processando dados...")
    contador += 1

#---------------------

#Exibir mensagem 5 vezes
message = "Bem-vindo ao Buscante!"

for i in range(5):
    print(message)

#---------------------

#Calcular soma total de valores
valores = [10, 20, 30, 40, 50]
soma = 0


for valor in valores:
    soma += valor
print(soma)


for valor in valores:
    soma += valor
    print(f"Valor atual: {valor} | Soma até agora: {soma}")

print(f"Soma final: {soma}")

#---------------------

#Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)


#---------------------

#exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrad
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"\nLivro encontrado: {livro}\n")
        break

#---------------------


estoque = 5
estoq =5

while estoque > 0:
    estoque = estoque - 1
    print(f"Venda realizada! Estoque restante {estoque}")
print("Estoque esgotado")



for o in range(5):
    estoq -= 1
    print(f"Venda realizada! Estoque restante {estoq}")

print("Estoque esgotado\n\n")


#---------------------
#exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!"

for y in range(10, 0, -1):
    if y % 2 == 0:
        print(f"Faltam apenas {y} segundos - Não perca essa oportunidade!")
    else:
        if y == 1:
            print(f"A contagem continua: {y} segundo restante.")
        else:
            print(f"A contagem continua: {y} segundos restantes.")

print(f"Aproveite a promoção agora!\n")


#Exemplo com apenas um print
for x in range(10, 0, -1):
    if x % 2 == 0:
        mens = f"Faltam apenas {x} segundos - Não perca essa oportunidade!"
    elif x == 1:
        mens = f"A contagem continua: {x} segundo restante."
    else:
        mens = f"A contagem continua: {x} segundos restantes."

    print(mens)
print()


#---------------------

# exibir somente os livros que possuem estoque disponível

livrs = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livrs:
    if livro["estoque"] > 0:
        print(f"Livro disponível: {livro['nome']}")
print()

#---------------------

#While True = continua pedindo dados até que o usuário insira informações válidas e caso forem validas finaliza no Break
# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.

while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")


    if len(nome_usuario) < 5:
        print(f"O nome de usuário precisa de no mínimo 5 caracteres!")
        continue

    if len(senha) < 8:
        print(f"A senha precisa ter no mínimo 8 caracteres!")
        continue

    print(f"Cadastro realizado com sucesso!")
    break