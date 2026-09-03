cpf =  input("Digite seu CFP: ")
qnt_numeros = 11

def validador(cpf, qnt_numeros):
    cpf = str(cpf)
    so_tem_numeros = cpf.isdigit()
    tamanho_certo = len(cpf) == qnt_numeros

    return so_tem_numeros and tamanho_certo


if validador(cpf, qnt_numeros):
    print("CPF válido")
else:
    print("CPF inválido")