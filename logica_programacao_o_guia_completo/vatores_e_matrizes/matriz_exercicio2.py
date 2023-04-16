"""
    Leia uma matriz 4x4 e apresente:
     O somatorio da segunda linha da matriz
     o somatorio da segunda coluna da matriz
     o somatorio de todos elementos da matriz
"""

import numpy

TAMANHO = 4

matriz = numpy.empty([TAMANHO, TAMANHO], dtype=numpy.int32)

for linha in range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        print("Digite o valor da linha ", linha, " e da coluna ", coluna, ": ")
        matriz[linha][coluna] = int(input())

soma_linha = 0
soma_coluna = 0
soma_total = 0

for linha in range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        soma_total += matriz[linha][coluna]
        if linha == 1:
            soma_linha += matriz[coluna][linha]
        if coluna == 1:
            soma_coluna += matriz[coluna][linha]

print("Soma total: ", soma_total)
print("Soma linha: ", soma_linha)
print("Soma coluna: ", soma_coluna)

