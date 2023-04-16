import numpy

vetor = numpy.empty(5)

vetor[1] = 10
vetor[2] = 20
vetor[3] = 30
vetor[4] = 40
vetor[5] = 50

for posicao in range(0, 5):
    print(vetor[posicao])
