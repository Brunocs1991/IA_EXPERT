"""
(Contador) Escrever um algoritimo que lê 5 valores para a variável a, um de cada vez,
e conta quanto desses valores são negativos. Após a leitura o programa deve mostrar
a quantidade de números negativos
"""

negativos = 0
for contador in range(1, 6):
    print('Digite o valor ', contador)
    valor = float(input())
    if valor < 0:
        negativos += 1
print('Quantidade de números negativos: ', negativos)