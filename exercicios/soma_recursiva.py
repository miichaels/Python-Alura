

def soma_recursiva(n):
    if n == 1:  # Condição de parada: se n for 1, retorna 1
        return 1
    return n + soma_recursiva(n - 1) # Chama a função novamente com n-1 e soma o n atual

numero = int(input("Digite um número: "))
print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}")