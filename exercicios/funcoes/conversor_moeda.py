
def converter_dolar(valor_em_reais):
    taxa_de_cambio = 5.45
    return valor_em_reais / taxa_de_cambio


valor = float(input("Digite o valor em reais: "))

valor_convertido = converter_dolar(valor)

print(f"Valor convertido em dólar: US$ {valor_convertido:.2f}")