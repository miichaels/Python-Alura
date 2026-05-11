def saldacao(hora):
    if hora <= 12:
        return "Bom dia"
    elif hora <= 18:
        return "Boa tarde"
    else:
        return "Boa noite"


hora_atual = int(input('Digite uma hora atual (0-23): '))

print(saldacao(hora_atual))