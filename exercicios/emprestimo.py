renda_mensal = float(input('Digite o valor da renda mensal: '))

parcela_desejada = float(input('Digite o valor da parcela desejada: '))


if renda_mensal > 2.000 and parcela_desejada <= 0.3 * renda_mensal :
    print('Emprestimo aprovado!')
elif renda_mensal <= 2.000:
    print('Emprestimo negado: renda insuficiente!')
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")