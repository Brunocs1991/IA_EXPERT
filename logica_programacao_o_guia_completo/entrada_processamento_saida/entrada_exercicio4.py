print('Digite o numero total de prestações: ')
numero_total_de_prestacoes = float(input())
print('Digite a quantidade total de prestações paga: ')
numero_prestacoes_pagas = float(input())
print('Digite o valor de cada prestação: ')
valor_prestacao = float(input())

total_pago = valor_prestacao * numero_prestacoes_pagas
saldo_devedor = valor_prestacao * (numero_total_de_prestacoes - numero_prestacoes_pagas)

print('Total pago: ', total_pago)
print('Saldo devedor: ', saldo_devedor)
