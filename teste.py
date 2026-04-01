def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo >= 25 and tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")

configurar_tempo_foco()

print()

usuarioAdmin = "admin"
senhaAdmin = "1234"

usuario = (input("Digite seu usuário: "))
senha = (input("Digite sua senha: "))

if usuario == usuarioAdmin and senha == senhaAdmin:
    print("Usuário e senha corretas, bem-vindo!\n")
else:
    print("Usuário e senha incorreto, tente novamente!\n")



idade = (int(input("Digite a sua idade: ")))
if idade  <= 12:
    print("Classificação - Criança\n")
elif idade >= 13 and idade  <=18:
    print("Classificação - Adolescente\n")
else:
    print("Classificação - Adulto\n")

print()