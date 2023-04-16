"""
Leia duas matrizes A e B com dimensoes 3 x 3. crie uma matrix c de
mesma dimensao que seja a soma de a + b. no final imprimir a matriz c
"""

import numpy

TAMANHO = 3

matrizA = numpy.empty([TAMANHO, TAMANHO])
matrizB = numpy.empty([TAMANHO, TAMANHO])
matrizC = numpy.empty([TAMANHO, TAMANHO])

print("Leitura da matriz A")
for linha in range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        print("Digite o valor da linha ", linha, " e coluna ", coluna, ":")
        matrizA[linha][coluna] = int(input())

print("Leitura da matriz B")
for linha in range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        print("Digite o valor da linha ", linha, " e coluna ", coluna, ":")
        matrizB[linha][coluna] = int(input())

for linha in range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]

print(matrizC)
