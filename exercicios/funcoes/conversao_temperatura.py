
temperatura = int(input("Digite a temperatura em graus Celsius: "))

temperatura = (temperatura * 9/5) +32

print(f"Temperatura: {temperatura} °F")

#-------------------------------------------------------------------S


#Com função

def conversor_temperatura(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = conversor_temperatura(temp)

print(f"Temperatura: {fahrenheit} °F")



