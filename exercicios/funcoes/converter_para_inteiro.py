
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]


def converter(lista):
    return [int(n) for n in lista]

print(converter(telefones))

#-------------------------------

def converter_telefones(lista):
    return [int(telefone) for telefone in lista]

def verifica_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro de conversão."

    return "Todos os números foram convertidos corretamente!"

telefones_convertidos = converter_telefones(telefones)

print(verifica_tipos(telefones_convertidos))


x = 10
print(isinstance(x, int))

nome = "Maria"
print(isinstance(nome, str))