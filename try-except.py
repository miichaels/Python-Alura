from logging import exception

numeros = [10,20,30,40,50]

soma = 0

# Soma valores da lista
try:
    for numero in numeros:
        soma += numero

    print(f"Soma total {soma}" )

except exception as e:
    print("Erro: valor inválido na lista")




# Média dos valores da lista
lista_valores = [15,20,25,30,35, "a"]
soma_valores = 0
try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores/len(lista_valores)
    print(f"Média dos valores da lista {media}")
except ZeroDivisionError:
    print(f"A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")