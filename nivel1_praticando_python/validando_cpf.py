
cpf =  input("Digite seu CPF: ")
qnt_numeros = 11


if cpf.isdigit() == False:
    print("Erro: O CPF deve conter apenas números.")
elif len(cpf) != qnt_numeros:
    print("Erro: O CPF deve ter exatamente 11 dígitos.")
else:
    print("CPF válido.")
