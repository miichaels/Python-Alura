pessoa = [
    {"nome": "Pedro", "idade": 10, "empregado": True},
    {"nome": "Gabete", "idade": 20, "empregado": True },
    {"nome": "Maria", "idade": 30, "empregado": False },
    {"nome": "Caleb", "idade": 40, "empregado": False },
]

#listar pessoas do dicionario pessoa maiores de 18 anos
def listar_pessoas():
    for listar in pessoa:
        if listar["idade"] >= 18:
            print(f"Nome: {listar['nome']}, idade: {listar['idade']}, empregado: {listar['empregado']}")



def atualizar_pessoa():
    nome_busca = input("Digite o nome da pessoa que deseja atualizar: ")
    for listar in pessoa:
        if listar["nome"] == nome_busca:
            if listar["empregado"]:
                listar["empregado"] = False
                print(f"Nome: {listar['nome']} agora está desempregado.")
            else:
                print(f"{listar["nome"]} já está desempregado.")
            return



listar_pessoas()
print()
atualizar_pessoa()
listar_pessoas()

