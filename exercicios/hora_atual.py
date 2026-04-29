hora_atual = int(input('Digite a hora atual (formato 24 horas): '))

if 8 <= hora_atual < 18:
    print('Horario permitido')
else:
    print('Horario não permitido')