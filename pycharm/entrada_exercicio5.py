print('Digite o tempo de viagem: ')
tempo = float(input())
print('Digite a velocidade média: ')
velocidade = float(input())

distancia = tempo * velocidade
litros = distancia / 12

print('Velocidade media: ', velocidade)
print('Tempo: ', tempo)
print('Distância percorrida: ', distancia)
print('Litros: ', litros)
